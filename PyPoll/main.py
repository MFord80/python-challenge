import os
import csv
from typing import OrderedDict

# Path to collect data
file = os.path.join("Resources", "election_data.csv")

# Define variables
tot_votes = 0
candidates = []
votes = []

# Define search funciton
def search(list, cell):
    for i in range(len(list)):
        if list[i] == cell:
            return True
    return False

# Read in the CSV file
with open(file) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Adjust for header
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:

    #Total months count
        tot_votes += 1

    #Create candidates list
        if search(candidates, row[2]):
            continue
        else:
            candidates.append(row[2])

           

#Candidate vote tallies
for x in candidates:
    print(x)

print(tot_votes) 

x = 1

set_ = [2,2,3]
print(set_)
set_[x] += 1
print(set_)





## Search function adapted from this page: https://appdividend.com/2022/05/30/how-to-find-element-in-list-in-python/
