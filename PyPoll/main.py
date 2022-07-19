import os
import csv

# Path to collect data
file = os.path.join("Resources", "election_data.csv")

# Define variables
tot_votes = 0
candidates = []
votes = []
percentage = []

# Read in the CSV file
with open(file) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Adjust for header
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:

    #Total votes count
        tot_votes += 1

    #Create candidates list (with 1 initial vote tallied)
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(1)
    #Tally votes by assigning 
        else:
            x = candidates.index(row[2])
            votes[x] += 1

# Calculate percentage of total votes by looping through vote tallies
for i in votes:
    individual_percentage = i/tot_votes
    percentage.append(round(individual_percentage * 100, 3))

# To determine winner
most_votes = max(votes)
winner_index = votes.index(most_votes)
winner = candidates[winner_index]

# Print analysis to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {tot_votes}")
print("------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percentage[i]}% ({votes[i]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

#Export analysis to .txt
file = os.path.join("Analysis", "results.txt")

with open(file, "w") as writer:
    writer.write("Election Results\n------------------------\n")
    writer.write(f"Total Votes: {tot_votes}\n")
    writer.write("------------------------\n")
    for i in range(len(candidates)):
        writer.write(f"{candidates[i]}: {percentage[i]}% ({votes[i]})\n")
    writer.write("------------------------\n")
    writer.write(f"Winner: {winner}\n")
    writer.write("------------------------")
   



