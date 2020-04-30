#!/usr/bin/env python3

import cgi

print('HTTP/1.0 200 OK')
print('Content-Type: text/html')
print()

form = cgi.FieldStorage()

print('''
<h1>Welcome to yet another ND sports trivia quiz</h1>
<form>
	<h2>YO what's your name?<h2><input type="text" name="user">
	<h2 class="question">Who is the Karen and Kevin Keyes head women's basketball coach?</h2>
		<h3 class="answer"><input type="radio" name="ans1" value="a">
			a) Muffet McGraw
		</h3>
		<h3 class="answer"><input type="radio" name="ans1" value="b">
			b) Mike Brey
		</h3>
		<h3 class="answer"><input type="radio" name="ans1" value="c">
			c) Niele Ivey
		</h3>
		<h3 class="answer"><input type="radio" name="ans1" value="d">
			d) Carol Owens
		</h3>
	<h2 class="question">Which player was drafted first in the 2020 NFL draft?</h2>
		<h3 class="answer"><input type="radio" name="ans2" value="a">
			a) Cole Kmet
		</h3>
		<h3 class="answer"><input type="radio" name="ans2" value="b">
			b) Julian Okwara
		</h3>
		<h3 class="answer"><input type="radio" name="ans2" value="c">
			c) Ian Book
		</h3>
		<h3 class="answer"><input type="radio" name="ans2" value="d">
			d) Chase Claypool
		</h3>
	<h2 class="question">Which track and field athlete is a reigning national champ?</h2>
		<h3 class="answer"><input type="radio" name="ans3" value="a">
			a) Anna Rohrer
		</h3>
		<h3 class="answer"><input type="radio" name="ans3" value="b">
			b) Yared Nuguse
		</h3>
		<h3 class="answer"><input type="radio" name="ans3" value="c">
			c) Danny Kilrea
		</h3>
		<h3 class="answer"><input type="radio" name="ans3" value="d">
			d) Jessica Harris
		</h3>
	<h2 class="question">Which team won Notre Dame's most recent national championship?</h2>
		<h3 class="answer"><input type="radio" name="ans4" value="a">
			a) Fencing
		</h3>
		<h3 class="answer"><input type="radio" name="ans4" value="b">
			b) Women's Basketball
		</h3>
		<h3 class="answer"><input type="radio" name="ans4" value="c">
			c) Football
		</h3>
		<h3 class="answer"><input type="radio" name="ans4" value="d">
			d) Men's Cross Country
		</h3>
	<h2 class="question">Which sports team does not compete in gold helmets?</h2>
		<h3 class="answer"><input type="radio" name="ans5" value="a">
			a) Football
		</h3>
		<h3 class="answer"><input type="radio" name="ans5" value="b">
			b) Lacrosse
		</h3>
		<h3 class="answer"><input type="radio" name="ans5" value="c">
			c) Fencing
		</h3>
		<h3 class="answer"><input type="radio" name="ans5" value="d">
			d) Swimming
		</h3>
	<input type="submit" value="Submit">
</form>
''')

if 'user' in form:
	print('<h2>Hi {}, here are your results:</h2>'.format(form['user'].value))
	numcorrect = 0

if form.getvalue('ans1') == 'c' :
	print('''<h2>1) correct</h2><h3>thank you for staying up to date on ND women's basketball knowledge</h3>''')
	numcorrect += 1
elif form.getvalue('ans1') == 'a' or form.getvalue('ans1') == 'b' or form.getvalue('ans1') == 'd':
	print('''<h2>1) wrong</h2><h3>yikes you really need to follow women's basketball a little more closely</h3>''')
if form.getvalue('ans2') == 'a' :
	print('''<h2>2) correct</h2><h3>GO BEARS</h3>''')
	numcorrect += 1
elif form.getvalue('ans2') == 'b' or form.getvalue('ans2') == 'c' or form.getvalue('ans2') == 'd':
	print('''<h2>2) wrong</h2><h3>there's literally nothing else going on and you still didn't watch the draft? lame</h3>''')
if form.getvalue('ans3') == 'b' :
	print('''<h2>3) correct</h2><h3>Yared is the goat. need i say more?</h3>''')
	numcorrect += 1
elif form.getvalue('ans3') == 'a' or form.getvalue('ans3') == 'c' or form.getvalue('ans3') == 'd':
	print('''<h2>3) wrong</h2><h3>yikes you really need to follow track a little more closely</h3>''')
if form.getvalue('ans4') == 'b' :
	print('''<h2>4) correct</h2><h3>shoutout 2018 women's basketball team!! so iconic, so talented, so amazing</h3>''')
	numcorrect += 1
elif form.getvalue('ans4') == 'a' or form.getvalue('ans4') == 'c' or form.getvalue('ans4') == 'd':
	print('''<h2>4) wrong</h2><h3>it's only been two years and you've already forgotten? SAD!</h3>''')
if form.getvalue('ans5') == 'd' :
	print('''<h2>5) correct</h2><h3>Swimmers don't wear helmets and their swim caps are navy</h3>''')
	numcorrect += 1
elif form.getvalue('ans5') == 'a' or form.getvalue('ans5') == 'b' or form.getvalue('ans5') == 'c':
	print('''<h2>5) wrong</h2><h3>the golden helmets are iconic - pay more attention to them</h3>''')

if 'user' in form:
	print('\n')
	if numcorrect == 5:
		print('''<h2>congratulations! you know some pretty basic trivia about notre dame athletics</h2><h3>5/5 correct</h3>''')
	if numcorrect == 4:
		print('''<h2>80% is normally a decent score but in systems, that's a D. oops</h2><h3>4/5 correct</h3>''')
	if numcorrect == 3:
		print('''<h2>mediocre score, mediocre knowledge. try harder next time please</h2><h3>3/5 correct</h3>''')
	if numcorrect == 2:
		print('''<h2>you failed, but this semester we'll just call it no credit. lucky you!</h2><h3>2/5 correct</h3>''')
	if numcorrect == 1:
		print('''<h2>you failed, but this semester we'll just call it no credit. lucky you!</h2><h3>1/5 correct</h3>''')
	if numcorrect == 0:
		print('''<h2>sorry, you're trash. please leave nd until you learn to follow sports</h2><h3>0/5 correct</h3>''')
