# Part 1
import os
import csv

os.system("cls")
 

# set path for file
filepath = os.path.join("Data","election_data_2.csv")
newfilepath = os.path.join("Data","election_data_2_results.csv")

candidates = []
votes = []
voteresults = []
votePercent = []
j = []

# create a list of candiddates

#print (candidates)

# open the csv

with open(filepath, 'r', newline="") as csvfile:

    csvReader = csv.reader(csvfile, delimiter=",")
    
    next(csvReader,None)

    for x in csvReader:
        if x[2] not in candidates:
            #Create candiate list
            candidates.append(x[2])
        else:
            votes.append(x[2])
    print (candidates)
    #print (votes)
    #print (votes[1:5])
    # this provides the number of occurrences of "Khan" in the vote list
    j.append(votes.count('Khan'))
    # I am trying to iterate through the list of candidates capture the number of occurrences my vote list
    for i in candidates:
        # print (i)
        j.append(votes.count('candidates[i]'))
        print (j)
    
   