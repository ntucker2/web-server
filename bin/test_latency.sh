#!/bin/bash

echo "\n\nbrowse request, 1 hammer, 1 throw" >> testnew1.txt
for i in {1..10}
do
	./bin/thor.py http://ntucker2.codes:9111/html >> testnew1.txt
done

echo "\n\nbrowse request, 1 hammer, 5 throws" >> testnew2.txt
for i in {1..10}
do
	./bin/thor.py -t 5 http://ntucker2.codes:9111/html >> testnew2.txt
done

echo "\n\nbrowse request, 5 hammers, 1 throw" >> testnew3.txt
for i in {1..10}
do
	./bin/thor.py -h 5 http://ntucker2.codes:9111/html >> testnew3.txt
done

echo "\n\nbrowse request, 5 hammers, 5 throws" >> testnew4.txt
for i in {1..10}
do
	./bin/thor.py -t 5 -h 5 http://ntucker2.codes:9111/html >> testnew4.txt
done

echo "\n\ntext request, 1 hammer, 1 throw" >> testnew1.txt
for i in {1..10}
do
	./bin/thor.py http://ntucker2.codes:9111/text/lyrics.txt >> testnew1.txt
done

echo "\n\ntext request, 1 hammer, 5 throws" >> testnew2.txt
for i in {1..10}
do
	./bin/thor.py -t 5 http://ntucker2.codes:9111/text/lyrics.txt >> testnew2.txt
done

echo "\n\ntext request, 5 hammers, 1 throw" >> testnew3.txt
for i in {1..10}
do
	./bin/thor.py -h 5 http://ntucker2.codes:9111/text/lyrics.txt >> testnew3.txt
done

echo "\n\ntext request, 5 hammers, 5 throws" >> testnew4.txt
for i in {1..10}
do
	./bin/thor.py -t 5 -h 5 http://ntucker2.codes:9111/text/lyrics.txt >> testnew4.txt
done

echo "\n\nimage request, 1 hammer, 1 throw" >> testnew1.txt
for i in {1..10}
do
	./bin/thor.py http://ntucker2.codes:9111/images/c.jpg >> testnew1.txt
done

echo "\n\nimage request, 1 hammer, 5 throws" >> testnew2.txt
for i in {1..10}
do
	./bin/thor.py -t 5 http://ntucker2.codes:9111/images/c.jpg >> testnew2.txt
done

echo "\n\nimage request, 5 hammers, 1 throw" >> testnew3.txt
for i in {1..10}
do
	./bin/thor.py -h 5 http://ntucker2.codes:9111/images/c.jpg >> testnew3.txt
done

echo "\n\nimage request, 5 hammers, 5 throws" >> testnew4.txt
for i in {1..10}
do
	./bin/thor.py -t 5 -h 5 http://ntucker2.codes:9111/scripts/cowsay.sh >> testnew4.txt
done

echo "\n\ncowsay request, 1 hammer, 1 throw" >> testnew1.txt
for i in {1..10}
do
	./bin/thor.py http://ntucker2.codes:9111/scripts/cowsay.sh >> testnew1.txt
done

echo "\n\ncowsay request, 1 hammer, 5 throws" >> testnew2.txt
for i in {1..10}
do
	./bin/thor.py -t 5 http://ntucker2.codes:9111/scripts/cowsay.sh >> testnew2.txt
done

echo "\n\ncowsay request, 5 hammers, 1 throw" >> testnew3.txt
for i in {1..10}
do
	./bin/thor.py -h 5 http://ntucker2.codes:9111/scripts/cowsay.sh >> testnew3.txt
done

echo "\n\ncowsay request, 5 hammers, 5 throws" >> testnew4.txt
for i in {1..10}
do
	./bin/thor.py -t 5 -h 5 http://ntucker2.codes:9111/images/c.jpg >> testnew4.txt
done

echo "\n\nhellopy request, 1 hammer, 1 throw" >> testnew1.txt
for i in {1..10}
do
	./bin/thor.py http://ntucker2.codes:9111/scripts/hello.py >> testnew1.txt
done

echo "\n\nhellopy request, 1 hammer, 5 throws" >> testnew2.txt
for i in {1..10}
do
	./bin/thor.py -t 5 http://ntucker2.codes:9111/scripts/hello.py >> testnew2.txt
done

echo "\n\nhellopy request, 5 hammers, 1 throw" >> testnew3.txt
for i in {1..10}
do
	./bin/thor.py -h 5 http://ntucker2.codes:9111/scripts/hello.py >> testnew3.txt
done

echo "\n\nhellopy request, 5 hammers, 5 throws" >> testnew4.txt
for i in {1..10}
do
	./bin/thor.py -t 5 -h 5 http://ntucker2.codes:9111/scripts/hello.py >> testnew4.txt
done
