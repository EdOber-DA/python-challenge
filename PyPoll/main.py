# --------------------------------------------
# --- Python Challenge - PyBank            ---
#---------------------------------------------

# --------------------------------------------
# INITIALIZATION
# --------------------------------------------
# import libraries
import os, csv

# Initialize variables for the Analysis
candidate = {}        # Empty set that will contain the candidate names and vote counters

# -----------------------------------
# --- Setup Input File Processing ---
# -----------------------------------

# Set Path to the data file in the Resources folder
PollData_csv_path = os.path.join('Resources', 'election_data.csv')

# Open the data file with Read capabilities
with open(PollData_csv_path, 'r') as csvfilein:

    # Read the data, and since it is a CSV, Split the data on comma delimiters
    PollData_row = csv.reader(csvfilein, delimiter=',')

    # Store the initial header line
    PollData_Header = next(PollData_row)

# -----------------------------------
# --- Main Processing Loop        ---
# -----------------------------------
    # Loop through the data 
    for row in PollData_row:

        # Read the Voter_ID, County, and Candidate for the current row for readability of the code below
        # Note: Voter_Id and County are being read only for future use in some extended work later on County tally's and voter audits
        Voter_ID = row[0]
        County = row[1]
        Candidate = row[2]

        if candidate.get(Candidate) == None:
                candidate[Candidate] = 1
        else: candidate[Candidate] +=1 

# ------------------------------
# --- Finish and Output Data ---
# ------------------------------
print(f'candidate list and votes = {candidate}')

sorted_by_votes = sorted(candidate.items(), key= lambda vote_count: vote_count[1], reverse=True)

print(f'sorted by votes= {sorted_by_votes}')

# Print to Terminal
#print(f"Financial Analysis\n"
#    f"----------------------------\n"
#    f"Total Months: {Total_Months}\n"
#    f"Total: ${Total_Profit_Loss:,}\n"
#    f"Average Change: ${float(Total_Profit_Loss/Total_Months):,.2f}\n"
#    f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_Amt:,})\n"
#    f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease_Amt:,})")

# Set Path to the output file in the analysis folder
#BankDataAnalysis_csv_path = os.path.join('analysis', 'budget_data_analysis.csv')

# Open the data file with write capabilities
#with open(BankDataAnalysis_csv_path, 'w',newline="") as csvfileout:
#     csvwriter = csv.writer(csvfileout, delimiter=',')
#     csvwriter.writerow(["Financial Analysis"])
#     csvwriter.writerow(["----------------------------"])
#     csvwriter.writerow([f"Total Months: {Total_Months}"])
#     csvwriter.writerow([f"Total: ${Total_Profit_Loss:,}"])
#     csvwriter.writerow([f"Average Change: ${float(Total_Profit_Loss/Total_Months):,.2f}"])
#     csvwriter.writerow([f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_Amt:,})"])
#     csvwriter.writerow([f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease_Amt:,})"])