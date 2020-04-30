#!/bin/bash

#echo "sttest1 is forking, single" >> sttest1.txt
#echo "small file 1" >> sttest1.txt
#for i in {1..10}
#do
#	./bin/thor.py -t 4 -h 4 http://ntucker2.codes:9114/lil1.img >> sttest1.txt
#done

#echo "small file 2" >> sttest1.txt
#for i in {1..10}
#do
#	./bin/thor.py -t 4 -h 4 http://ntucker2.codes:9114/lil2.img >> sttest1.txt
#done

#echo "mid file 1" >> sttest1.txt
#for i in {1..10}
#do
#	./bin/thor.py -t 4 -h 4 http://ntucker2.codes:9115/mid1.img >> sttest1.txt
#done

#echo "mid file 2" >> sttest1.txt
#for i in {1..10}
#do
#	./bin/thor.py -t 4 -h 4 http://ntucker2.codes:9115/mid2.img >> sttest1.txt
#done

#echo "big file 1" >> sttest1.txt
#for i in {1..4}
#do
#	./bin/thor.py -t 2 -h 2 http://ntucker2.codes:9112/big1.img >> sttest1.txt
#done

echo "big file 2" >> sttest1.txt
#for i in {1..10}
#do
./bin/thor.py -t 2 -h 2 http://ntucker2.codes:9113/big2.img >> sttest1.txt
#done
