#!/bin/bash

git clone https://github.com/shrutipoojary27/Franklin.git

# changing directory into the repo

cd ./Franklin

# add the rights to execute the scripts in this repo

chmod +x Frank* 
chmod +x *.py

# the for loop below executes all the scripts in the Repo and outputs a Csv file

for i in $(ls Frank*)
do
	./$i | awk -F ',' '{OFS="\t";print $1,$2,$3,$4,$5,$6}' >> Team_Franklin.csv
done

for j in $(ls *.py)
do
    python $j | awk -F ',' '{OFS="\t";print $1,$2,$3,$4,$5,$6}' >> Team_Franklin.csv
done
