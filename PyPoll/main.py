# Part 1
import os
import csv

os.system("cls")
 

# set path for input and output file
filepath = os.path.join("Data","election_data_2.csv")
newfilepath = os.path.join("Data","election_data_2_results.csv")


# initialize lists
candidates = []
votes = []
voteresults = []
votepercent = []




# open the csv

with open(filepath, 'r', newline="") as csvfile:

    csvReader = csv.reader(csvfile, delimiter=",")
    
    next(csvReader,None)
    # locate each unique candidate and create list of all votes
    for x in csvReader:
        if x[2] not in candidates:
            #Create candiate list
            candidates.append(x[2])
        else:
            votes.append(x[2])
    print (candidates)
    
    # count the votes per candidate
        
    for i in range(len(candidates)):
      
        voteresults.append(votes.count(candidates[i]))

        print(voteresults)
    # arrive at total votes cast
    totalvotes = sum(voteresults)
    # create a dict of votes per candidate
    j = dict(zip(candidates, voteresults))
    print (j)

    k = dict(zip(candidates,votepercent,voteresults))
    print (k)
    # find the candidate with the most popular votes
    winner = max(j, key=j.get)
    print (winner)
    
    # calculate the vote percent
    for i in range(len(voteresults)):
        # print (i)
        percent = round((voteresults[i]/totalvotes) * 100,2)
        # print (percent)
        votepercent.append(percent)
    print (votepercent)

    
    cleanCSV = zip(candidates,votepercent,voteresults)

    # print results to the console

    print ("Election Results")
    print ("")
    
    print ('*'*80)
    print ('Total Votes: ' + str(totalvotes))
    print ('*'*80)
    print ("")

    for i in range(len(candidates)):
        # print (i)
         print ((candidates[i]) + " " + str(votepercent[i]) +"%" + " "  + str(voteresults[i] ))
        # print (percent)
    print ("")
    print ('*'*80)
    print ("Winner: " + winner)
    print ("")
    print ('*'*80)

        
    
   
    #write to output file
    with open(newfilepath, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Candidate","Vote Percentage","Total Votes"])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)

    
       