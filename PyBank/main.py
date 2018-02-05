# add necessary libraries
import csv
import os

# clear screen 
os.system("cls")
 

# set path for input and output file
filepath = os.path.join("Data","budget_data_2.csv")
newfilepath = os.path.join("Data","budget_data_2_results.csv")


#set initial variables
months = []
revenue = []
newlist = []

#open data file as csv
with open(filepath, 'r', newline="") as csvfile:

    csvReader = csv.reader(csvfile, delimiter=",")
    
    next(csvReader,None)
    for x in csvReader:
        months.append(x[0].split('-'))
        revenue.append(x[1])
        
    # create 2 separate lists from months; 1 list with years and another list with months
    y, m = zip(*months)
    # create a new list with elements month,year
    for i in range(len(months)):
        newlist.append(m[i] + "-" + y[i])
    
    #arrive at total months for data set
    totalmonths = len(months)
    #arrive at total revenue for data set
    totalrevenue = sum(int(r) for r in revenue)
    print ("Financial Analysis")
    print ("")
    print ("*"*80)
    print ("Total Months:" + " " + str(totalmonths))
    print ("Total Revenue:" + " " + "$" + str(totalrevenue))
    avg_change = round(totalrevenue/totalmonths,2)
    print ("Average Revenue Change:" + " " + "$" + str(avg_change))
    revenue_int = [int(i) for i in revenue]

# create dictionary list with month, year and revenue

j = dict(zip(newlist,revenue_int))
# print (j)

# find best month
best_month = max(j, key=j.get)
# find worst month
worst_month = min(j, key=j.get)
#  get the revenue for the best month
best_month_revenue = j[best_month]
# get the revenue for the worst month
worst_month_revenue = j[worst_month]

# print the results as part of the analysis
print ((best_month) + " " + "$" + str(best_month_revenue))
print ((worst_month) + " " + "$" + str(worst_month_revenue))

# print to a file
with open('finanalysis.txt', 'w') as f:
    print ("Financial Analysis", file=f)
    print ("", file=f)
    print ("*"*80, file=f)
    print ("Total Months:" + " " + str(totalmonths), file=f)
    print ("Total Revenue:" + " " + "$" + str(totalrevenue), file=f)
    print ("Average Revenue Change:" + " " + "$" + str(avg_change), file=f)
    print ((best_month) + " " + "$" + str(best_month_revenue), file=f)
    print ((worst_month) + " " + "$" + str(worst_month_revenue), file=f)
