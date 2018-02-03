# modules

import os
import csv

os.system("cls")  

# set path for file
filepath = os.path.join("Data","election_data_2.csv")

candidates = []
votes = []

# create a list of candiddates


#print (candidates)

# open the csv

with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #total the number of rows in csvreader
    #total_votes = sum(1 for row in csvreader)
    
    # decrement total_votes by 1 to not include file header
    #print (total_votes-1)
    #x = 1
    # arrive at number of candidates
    for x in csvreader:
        if x[2] not in candidates and x[2] != "Candidate":
            #Create candiate list
            candidates.append(x[2])
        elif x[2] != "Candidate":
            #Create list of votes per candidate
            votes.append(x[2])
    print (candidates) 
   # print (votes)
    


    

    #for x in votes

    # arrive at number of votes per candidate

    from collections import Counter
    input = votes
    print (type (input))
    print(votes[0:4])
    # print ("this is votes: " + votes)
    counted_votes = Counter(input)
    cv = counted_votes.items()
    print (cv)
    #results = [x for x,_ in counted_votes]
    #print (results)

    # print the candiate and results

    
    print ("*"*80)
    
    
    
    #total_votes = sum(1 for row in csvreader)

    #print (total_votes-1)

    #for item in counted_votes:
     #   print (str(item[0]) 


 

   
        

    #number_of_candidates = len(candidates)
    #print (number_of_candidates)
    #if x[2] == candidates[0]:
        

   #results
   
    
   #for row in csvreader:
       
        

   #print (row)
    #     number_of_votes = number_of_votes + 1  
     #   if row[2] == candidates[0]:
      #       
      #   elif row[2] == "Vestal":
       #      votes_for_vestal = votes_for_vestal + 1
        # elif row[2] == "Seth":
         #    votes_for_seth= votes_for_seth + 1
         #elif row[2] == "Cordin":
          #   votes_for_cordin= votes_for_cordin + 1
#number_of_votes = number_of_votes - 1 
#percentTorres = votes_for_torres/number_of_votes 
    
#print ("Total votes: " + str(number_of_votes))
#print (candidates[0] + " " + "{:.2%}".format(percentTorres) + " " +str(votes_for_torres))
#print (candidates[1] + " " + str(votes_for_vestal))
#print (candidates[2] + " " + str(votes_for_seth))
#print (candidates[3] + " " + str(votes_for_cordin))