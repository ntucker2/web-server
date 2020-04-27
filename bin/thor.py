#!/usr/bin/env python3

import concurrent.futures
import os
import requests
import sys
import time

# Functions

def usage(status=0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-h HAMMERS -t THROWS] URL
    -h  HAMMERS     Number of hammers to utilize (1)
    -t  THROWS      Number of throws per hammer  (1)
    -v              Display verbose output
    ''')
    sys.exit(status)

def hammer(url, throws, verbose, hid):
    ''' Hammer specified url by making multiple throws (ie. HTTP requests).

    - url:      URL to request
    - throws:   How many times to make the request
    - verbose:  Whether or not to display the text of the response
    - hid:      Unique hammer identifier

    Return the average elapsed time of all the throws.
    '''
    
    average = 0

    for inter in range(throws):
        #initializes the first time inside of the loop
        StartTime = time.time()
        #Same use of requests.get as from the hints and from reddit.py
        response = requests.get(url)
        #get throw time of the request so need to get it right after
        ThrowTime = time.time() - StartTime
        #print out the verbose response if desired
        if verbose:
            print(response.text)
        #print out each time there is a request
        print(f'Hammer: {hid}, Throw:  {inter}, Elapsed Time: {ThrowTime:.2f}')
        #get average to be able to get all the time
        average += ThrowTime
    #need to get the actual average to be able to display it and return it
    average = average / throws
    #print the total time for the average time for the individual useae of hammer
    print(f'Hammer: {hid}, AVERAGE  , Elapsed Time: {average:.2f}')
    #return
    return average

def do_hammer(args):
    ''' Use args tuple to call `hammer` '''
    #very similar to cracker in hulk.py
    return hammer(*args)

def main():
    
    #Initialization of the Three main variables for Thor.py
    hammers = 1
    throws  = 1
    verbose = False
    
    #Initialization of 'arguments' variable with all parts of command line
    arguments = sys.argv[1:]

    # Parse command line arguments

    #Checks no-length and immidiatnly goes to usage(1)
    if not len(arguments):
        usage(1)
    #More occuring outcome where command line is fully parsed
    else:
        while len(arguments) and arguments[0].startswith('-'):
            #Pops each argument individually to have stuff completed by it
            arg = arguments.pop(0)
            #fills hammers, throws, or verbose with proper values from command line
            if arg == '-h':
                hammers = int(arguments.pop(0))
            elif arg == '-t':
                throws = int(arguments.pop(0))
            elif arg == '-v':
                verbose = True
            else:
                usage(1)

    # Create pool of workers and perform throws
    
    #url is final argument so take it after parsing
    url = arguments.pop(0)
    
    #I used for __ in __ as it is one of the for implementations for python
    #and it is often paired with range()
    args = ((url, throws, verbose, hid) for hid in range(hammers))

    #very similar to how we completed smash in hulk.py
    with concurrent.futures.ProcessPoolExecutor(hammers) as executor:
        average = executor.map(do_hammer, args)
    
    TotalElapsed = 0
    NumElapsed = 0
    for inter in average:
        TotalElapsed += inter
        NumElapsed += 1

    print(f'TOTAL AVERAGE ELAPSED TIME: {(TotalElapsed/NumElapsed):.2f}')
    
    sys.exit(0)
    
# Main execution

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
