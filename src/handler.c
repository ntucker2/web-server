/* handler.c: HTTP Request Handlers */

#include "spidey.h"

#include <errno.h>
#include <limits.h>
#include <string.h>

#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>

/* Internal Declarations */
Status handle_browse_request(Request *request);
Status handle_file_request(Request *request);
Status handle_cgi_request(Request *request);
Status handle_error(Request *request, Status status);

/**
 * Handle HTTP Request.
 *
 * @param   r           HTTP Request structure
 * @return  Status of the HTTP request.
 *
 * This parses a request, determines the request path, determines the request
 * type, and then dispatches to the appropriate handler type.
 *
 * On error, handle_error should be used with an appropriate HTTP status code.
 **/
Status  handle_request(Request *r) {
    Status result;

    /* Parse request */
    if(parse_request(r) != 0) {
        result = HTTP_STATUS_BAD_REQUEST;
        goto handle_error;
    }

    /* Determine request path */
    r->path = determine_request_path(r->uri);
    if(!r->path){
        result = HTTP_STATUS_NOT_FOUND;
        goto handle_error;
    }

    debug("HTTP REQUEST PATH: %s", r->path);

    /* Dispatch to appropriate request handler type based on file type */
    struct stat s;
    if(stat(r->path, &s) < 0){
        result = HTTP_STATUS_NOT_FOUND;
    }

    if(S_ISDIR(s.st_mode)){
        result = handle_browse_request(r);
    }

    else if(s.st_mode & S_IXUSR){
        result = handle_cgi_request(r);
    }

    else if(s.st_mode){
        result = handle_file_request(r);
    }

    else{
        result = HTTP_STATUS_BAD_REQUEST;
    }

    log("HTTP REQUEST STATUS: %s", http_status_string(result));

    if(result != 0){
        goto handle_error;
    }

    return result;

handle_error:
    handle_error(r, result);
    return result;
}

/**
 * Handle browse request.
 *
 * @param   r           HTTP Request structure.
 * @return  Status of the HTTP browse request.
 *
 * This lists the contents of a directory in HTML.
 *
 * If the path cannot be opened or scanned as a directory, then handle error
 * with HTTP_STATUS_NOT_FOUND.
 **/
Status  handle_browse_request(Request *r) {
    /* Open a directory for reading or scanning */
    struct dirent **entries;
    int n = scandir(r->path, &entries, 0, alphasort);
    if(n < 0){
        debug("scandir no good: %s", strerror(errno));
        return HTTP_STATUS_NOT_FOUND;
    }

    /* Write HTTP Header with OK Status and text/html Content-Type */
    fprintf(r->stream, "HTTP/1.0 200 OK\r\n");
    fprintf(r->stream, "Content-Type: text/html\r\n");
    fprintf(r->stream, "\r\n");

    /* For each entry in directory, emit HTML list item */
    fprintf(r->stream, "<ul>\n");
    for(int i = 0; i < n; i++){
        if(!streq(entries[i]->d_name, ".")){
            if(streq(r->uri, "/")){
                fprintf(r->stream, "<li><a href=\"/%s\">%s</a></li>", entries[i]->d_name, entries[i]->d_name);
            }
            else{
                fprintf(r->stream, "<li><a href=\"%s/%s\">%s</a></li>\n", r->uri, entries[i]->d_name, entries[i]->d_name);
            }
            fprintf(r->stream, "\n");
        }
        free(entries[i]);
    }
    free(entries);
    fprintf(r->stream, "</ul>");

    /* Return OK */
    return HTTP_STATUS_OK;
}

/**
 * Handle file request.
 *
 * @param   r           HTTP Request structure.
 * @return  Status of the HTTP file request.
 *
 * This opens and streams the contents of the specified file to the socket.
 *
 * If the path cannot be opened for reading, then handle error with
 * HTTP_STATUS_NOT_FOUND.
 **/
Status  handle_file_request(Request *r) {
    /* Open file for reading */
    FILE *fs = fopen(r->path, "r");
    if(!fs){
        return HTTP_STATUS_NOT_FOUND;
    }

    /* Determine mimetype */
    char *mimetype = determine_mimetype(r->path);

    /* Write HTTP Headers with OK status and determined Content-Type */
    fprintf(r->stream, "HTTP/1.0 200 OK\r\n");
    fprintf(r->stream, "Content-Type: %s\r\n", mimetype);
    fprintf(r->stream, "\r\n");

    /* Read from file and write to socket in chunks */
    char buffer[BUFSIZ];
    size_t nread = fread(buffer, 1, BUFSIZ, fs);
    if(nread < 0){
        return HTTP_STATUS_NOT_FOUND;
    }
    while (nread > 0){
        if(!fwrite(buffer, 1, nread, r->stream)){
            goto fail;
        }
        nread = fread(buffer, 1, BUFSIZ, fs);
    }

    /* Close file, deallocate mimetype, return OK */
    fclose(fs);
    free(mimetype);
    return HTTP_STATUS_OK;

fail:
    /* Close file, free mimetype, return INTERNAL_SERVER_ERROR */
    fclose(fs);
    free(mimetype);
    return HTTP_STATUS_INTERNAL_SERVER_ERROR;
}

/**
 * Handle CGI request
 *
 * @param   r           HTTP Request structure.
 * @return  Status of the HTTP file request.
 *
 * This popens and streams the results of the specified executables to the
 * socket.
 *
 * If the path cannot be popened, then handle error with
 * HTTP_STATUS_INTERNAL_SERVER_ERROR.
 **/
Status  handle_cgi_request(Request *r) {
    FILE *pfs;

    /* Export CGI environment variables from request:
     * http://en.wikipedia.org/wiki/Common_Gateway_Interface */
    setenv("DOCUMENT_ROOT", RootPath, 1);
    setenv("QUERY_STRING", r->query, 1);
    setenv("REMOTE_ADDR", r->host, 1);
    setenv("REMOTE_PORT", r->port, 1);
    setenv("REQUEST_METHOD", r->method, 1);
    setenv("REQUEST_URI", r->uri, 1);
    setenv("SCRIPT_FILENAME", r->path, 1);
    setenv("SERVER_PORT", Port, 1);

    /* Export CGI environment variables from request headers */
    Header * h = r->headers;
    while(h!= NULL){
        if(streq(h->name, "Host")){
            setenv("HTTP_HOST", h->data, 1);
        }
        else if(streq(h->name, "Accept")){
            setenv("HTTP_ACCEPT", h->data, 1);
        }
        else if(streq(h->name, "Accept-Language")){
            setenv("HTTP_ACCEPT_LANGUAGE", h->data, 1);
        }
        else if(streq(h->name, "Accept-Encoding")){
            setenv("HTTP_ACCEPT_ENCODING", h->data, 1);
        }
        else if(streq(h->name, "Connection")){
            setenv("HTTP_CONNECTION", h->data, 1);
        }
        else if(streq(h->name, "User-Agent")){
            setenv("HTTP_USER_AGENT", h->data, 1);
        }

   // host, accept, accept language, accept encoding, connection
        h = h->next;
    }

    /* POpen CGI Script */
    pfs = popen(r->path, "r");
    if(!pfs){
        return HTTP_STATUS_INTERNAL_SERVER_ERROR;
    }

    /* Copy data from popen to socket */
    char buffer[BUFSIZ];
    while(fgets(buffer, BUFSIZ, pfs)){
        fputs(buffer, r->stream);
    };

    /* Close popen, return OK */
    pclose(pfs);
    return HTTP_STATUS_OK;
}

/**
 * Handle displaying error page
 *
 * @param   r           HTTP Request structure.
 * @return  Status of the HTTP error request.
 *
 * This writes an HTTP status error code and then generates an HTML message to
 * notify the user of the error.
 **/
Status  handle_error(Request *r, Status status) {
    const char *status_string = http_status_string(status);

    /* Write HTTP Header */
    fprintf(r->stream, "HTTP/1.0 %s\r\n", status_string);
    fprintf(r->stream, "Content-Type: text/html\r\n");
    fprintf(r->stream, "\r\n");

    /* Write HTML Description of Error*/
    fprintf(r->stream, "<h1>%s\n<h1>", status_string);
    fprintf(r->stream, "<h2>you really messed up this time</h2>");
    fprintf(r->stream, "<p>enjoy these vines to make up for it</p>");
    fprintf(r->stream, "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/k8crP4uXRpc\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>");
    fprintf(r->stream, "<audio controls><source src=\"dontlookinthisfolder/memez.m4a\"><div style=\"border: 1px solid black ; padding: 8px ;\">Sorry, your browser does not support the <audio> tag used in this demo.</div></audio>");
    /* Return specified status */
    return status;
}

/* vim: set expandtab sts=4 sw=4 ts=8 ft=c: */
