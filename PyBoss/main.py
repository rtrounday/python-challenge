# import libraries
import os
import csv
import datetime

# dictionary for state and 2 state abbreviation
us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}


# clear screen
os.system("cls")
 

# set path for input and output file
filepath = os.path.join("Data","employee_data1.csv")
newfilepath = os.path.join("Data","employee_data1_results.csv")

#create lists

employeename = []
empid = []
date = []
ssn = []
state = []
dob = []
maskssn = []
state_abbr = []

#open file defined in filepath

with open(filepath, 'r', newline="") as csvfile:

    csvReader = csv.reader(csvfile, delimiter=",")
    
    next(csvReader,None)
    for x in csvReader:
        empid.append(x[0])
        employeename.append(x[1].split(" "))
        date.append(x[2])
        ssn.append(x[3].split("-"))
        #ssn.append(x[3].replace("-", ""))
        state.append(x[4])

    # create 3 lists to hold SSN: f: first 3 digits, s: second 2 digits and l: last 4 digits
    f,s,l = zip(*ssn)
    
    # newssn = "*" * 3 + "-" + "*" * 2 + "-" + l[0]
    
    # create ssn list with masked ssn numbers
    for x in range(len(ssn)):
        maskssn.append("*" * 3 + "-" + "*" * 2 + "-" + l[x])
    #print (maskssn)
    
    # create dob in date format
    for i in range(len(date)):
        dob.append(datetime.datetime.strptime(date[i], '%m/%d/%Y').strftime('%m-%d-%y'))
   
    #create 2 separate lists first and last name

    firstname , lastname = zip(*employeename)
    
    # newstate = us_state_abbrev[state[0]]

    # find the 2 digit abbreviation for each state
    for j in range(len(state)):
       state_abbr.append(us_state_abbrev[state[j]])
    # print (state_abbr)

    cleanCSV = zip(empid,firstname,lastname,dob,maskssn,state_abbr)
  
  #write to output file
    with open(newfilepath, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["EmpId","First Name","Last Name",'DOB','SSN','State'])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)