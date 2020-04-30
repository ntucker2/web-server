#!/usr/bin/env python3

import cgi

print('HTTP/1.0 200 OK')
print('Content-Type: text/html')
print()

form = cgi.FieldStorage()

print('''
<h1>Which CS Prof are you, based on your answers to random questions</h1>
<h3>** this survey was made without knowing the professors' answers to any of these questions</h3>
<form>
   <h3>What's your name?<h3><input type="text" name="user">
   <h3 class="question">Where do you teach?</h3>
      <p class="answer"><input type="radio" name="ans1" value="a">
         a) Notre Dame
      </p>
      <p class="answer"><input type="radio" name="ans1" value="b">
         b) Notre Dame
      </p>
      <p class="answer"><input type="radio" name="ans1" value="c">
         c) Notre Dame
      </p>
      <p class="answer"><input type="radio" name="ans1" value="d">
         d) Notre Dame
      </p>
   <h3 class="question">What's your favorite dessert?</h3>
      <p class="answer"><input type="radio" name="ans2" value="a">
         a) Cheesecake
      </p>
      <p class="answer"><input type="radio" name="ans2" value="b">
         b) Apple Pie
      </p>
      <p class="answer"><input type="radio" name="ans2" value="c">
         c) Brownies
      </p>
      <p class="answer"><input type="radio" name="ans2" value="d">
         d) Chocolate Chip Cookies
      </p>
   <h3 class="question">What's your favorite movie?</h3>
      <p class="answer"><input type="radio" name="ans3" value="a">
         a) Shrek
      </p>
      <p class="answer"><input type="radio" name="ans3" value="b">
         b) The Emoji Movie
      </p>
      <p class="answer"><input type="radio" name="ans3" value="c">
         c) The Notebook
      </p>
      <p class="answer"><input type="radio" name="ans3" value="d">
         d) The Bee Movie
      </p>
   <h3 class="question">What's your favorite programming language?</h3>
      <p class="answer"><input type="radio" name="ans4" value="a">
         a) C++
      </p>
      <p class="answer"><input type="radio" name="ans4" value="b">
         b) R
      </p>
      <p class="answer"><input type="radio" name="ans4" value="c">
         c) Python
      </p>
      <p class="answer"><input type="radio" name="ans4" value="d">
         d) Matlab
      </p>
   <h3 class="question">If you could eat at one restaurant for the rest of your life, which would it be?</h3>
      <p class="answer"><input type="radio" name="ans5" value="a">
         a) Olive Garden
      </p>
      <p class="answer"><input type="radio" name="ans5" value="b">
         b) McDonalds
      </p>
      <p class="answer"><input type="radio" name="ans5" value="c">
         c) IHOP
      </p>
      <p class="answer"><input type="radio" name="ans5" value="d">
         d) SDH
      </p>
    <h3 class="question">What's your favorite animal?</h3>
      <p class="answer"><input type="radio" name="ans6" value="a">
         a) Red Panda
      </p>
      <p class="answer"><input type="radio" name="ans6" value="b">
         b) Naked Mole Rat
      </p>
      <p class="answer"><input type="radio" name="ans6" value="c">
         c) Python
      </p>
      <p class="answer"><input type="radio" name="ans6" value="d">
         d) Elephant
      </p>
    <h3 class="question">What's your favorite color?</h3>
      <p class="answer"><input type="radio" name="ans7" value="a">
         a) Magenta
      </p>
      <p class="answer"><input type="radio" name="ans7" value="b">
         b) Cyan
      </p>
      <p class="answer"><input type="radio" name="ans7" value="c">
         c) Yellow
      </p>
      <p class="answer"><input type="radio" name="ans7" value="d">
         d) Rainbow
      </p>
    <h3 class="question">Who's your favorite One Direction member?</h3>
      <p class="answer"><input type="radio" name="ans8" value="a">
         a) Louis Tomlinson
      </p>
      <p class="answer"><input type="radio" name="ans8" value="b">
         b) Niall Horan
      </p>
      <p class="answer"><input type="radio" name="ans8" value="c">
         c) Liam Payne
      </p>
      <p class="answer"><input type="radio" name="ans8" value="d">
         d) Harry Styles
      </p>
    <h3 class="question">What's your favorite ice cream flavor?</h3>
      <p class="answer"><input type="radio" name="ans9" value="a">
         a) Vanilla
      </p>
      <p class="answer"><input type="radio" name="ans9" value="b">
         b) Superman
      </p>
      <p class="answer"><input type="radio" name="ans9" value="c">
         c) Strawberry Garcia
      </p>
      <p class="answer"><input type="radio" name="ans9" value="d">
         d) Cookies and Creme
      </p>
    <h3 class="question">What's your favorite Oreo flavor?</h3>
      <p class="answer"><input type="radio" name="ans10" value="a">
         a) Gingerbread
      </p>
      <p class="answer"><input type="radio" name="ans10" value="b">
         b) Key Lime Pie
      </p>
      <p class="answer"><input type="radio" name="ans10" value="c">
         c) Peeps
      </p>
      <p class="answer"><input type="radio" name="ans10" value="d">
         d) Jelly Donut
      </p>
   <input type="submit" value="Submit">
</form>
''')



if 'user' in form:
    a = 0
    b = 0
    c = 0
    d = 0

if form.getvalue('ans1') == 'a' :
   a += 1
elif form.getvalue('ans1') == 'b':
    b += 1
elif form.getvalue('ans1') == 'c':
    c += 1
elif form.getvalue('ans1') == 'd':
    d += 1
if form.getvalue('ans2') == 'a' :
   a += 1
elif form.getvalue('ans2') == 'b':
    b += 1
elif form.getvalue('ans2') == 'c':
    c += 1
elif form.getvalue('ans2') == 'd':
    d += 1
if form.getvalue('ans3') == 'a' :
   a += 1
elif form.getvalue('ans3') == 'b':
    b += 1
elif form.getvalue('ans3') == 'c':
    c += 1
elif form.getvalue('ans3') == 'd':
    d += 1
if form.getvalue('ans4') == 'a' :
   a += 1
elif form.getvalue('ans4') == 'b':
    b += 1
elif form.getvalue('ans4') == 'c':
    c += 1
elif form.getvalue('ans4') == 'd':
    d += 1
if form.getvalue('ans5') == 'a' :
   a += 1
elif form.getvalue('ans5') == 'b':
    b += 1
elif form.getvalue('ans5') == 'c':
    c += 1
elif form.getvalue('ans5') == 'd':
    d += 1
if form.getvalue('ans6') == 'a' :
   a += 1
elif form.getvalue('ans6') == 'b':
    b += 1
elif form.getvalue('ans6') == 'c':
    c += 1
elif form.getvalue('ans6') == 'd':
    d += 1
if form.getvalue('ans7') == 'a' :
   a += 1
elif form.getvalue('ans7') == 'b':
    b += 1
elif form.getvalue('ans7') == 'c':
    c += 1
elif form.getvalue('ans7') == 'd':
    d += 1
if form.getvalue('ans8') == 'a' :
   a += 1
elif form.getvalue('ans8') == 'b':
    b += 1
elif form.getvalue('ans8') == 'c':
    c += 1
elif form.getvalue('ans8') == 'd':
    d += 1
if form.getvalue('ans9') == 'a' :
   a += 1
elif form.getvalue('ans9') == 'b':
    b += 1
elif form.getvalue('ans9') == 'c':
    c += 1
elif form.getvalue('ans9') == 'd':
    d += 1
if form.getvalue('ans10') == 'a' :
   a += 1
elif form.getvalue('ans10') == 'b':
    b += 1
elif form.getvalue('ans10') == 'c':
    c += 1
elif form.getvalue('ans10') == 'd':
    d += 1


if 'user' in form:
   print('\n')
   if a >= b and a >= c and a >= d:
      print('<h3 style="color: red">Hi {}, you are Dr. Matthew Morrison</h3>'.format(form['user'].value))
   elif b >= c and c >= d:
      print('<h3 style="color: red">Hi {}, you are Professor Ramzi Bualuan</h3>'.format(form['user'].value))
   elif c >= d:
      print('<h3 style="color: red">Hi {}, you are Dr. Peter Bui</h3>'.format(form['user'].value))
   else:
      print('<h3 style="color: red">Hi {}, you are Dr. Siddarth Joshi</h3>'.format(form['user'].value))

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
