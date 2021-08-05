 
#!/bin/bash  # This is a shebang to initialise the script by calling on bash interpreter

#the command below clones the team Franklin repo

git clone https://github.com/shrutipoojary27/Franklin.git

# changing directory into the repo

cd ./Franklin

# add the rights to execute the scripts in this repo

chmod +x Frank* 
 
# the for loop below executes all the scripts in the Repo and outputs a Csv file

for i in $(ls Frank*)
do
	./$i | awk -F ',' '{OFS="\t";print $1,$2,$3,$4,$5}' >> Team_Franklin.csv
done
