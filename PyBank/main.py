import os
import csv

# Path to collect data
file = os.path.join("Resources", "budget_data.csv")

# Define variables
tot_months = 0
tot_prof = 0
tot_change = 0
prev_prof = 1088983 #no change for first month
incr_change = 0  #incremental change
max_inc_change = 0
max_dec_change = 0
max_inc_month = 0
max_inc_amt = 0
max_dec_month = 0
max_dec_amt = 0

# Read in the CSV file
with open(file) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Adjust for header
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:

    #Total months count
        tot_months += 1

    #Total profit / loss sum
        tot_prof += int(row[1])

    #Incremental change is new profit / loss subtract previous profit / loss amount
        incr_change = int(row[1])-prev_prof
        tot_change += incr_change
        prev_prof = int(row[1])
    
    #Greatest increase calculation
        if incr_change > max_inc_change:
            max_inc_month = row[0]
            max_inc_amt = incr_change
            max_inc_change = incr_change

    #Greatest decrease calculation
        if incr_change < max_dec_change:
            max_dec_month = row[0]
            max_dec_amt = incr_change
            max_dec_change = incr_change


#Average change calculation (-1 as there is no change for first month)
avg_change = tot_change / (tot_months-1)

#Print results to terminal
print("Financial Analysis\n--------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${tot_prof}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {max_inc_month} (${max_inc_amt})")
print(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec_amt})")

#Export results to .txt
file = os.path.join("Analysis", "results.csv")

with open(file, "a") as writer:
    writer.write("Financial Analysis\n--------------------------------\n")
    writer.write(f"Total Months: {tot_months}\n")
    writer.write(f"Total: ${tot_prof}\n")
    writer.write(f"Average Change: ${round(avg_change, 2)}\n")
    writer.write(f"Greatest Increase in Profits: {max_inc_month} (${max_inc_amt})\n")
    writer.write(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec_amt})")