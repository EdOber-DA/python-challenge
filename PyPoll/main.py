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
Total_Votes = 0       # Total Vote count 
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

        # Add Votes
        Total_Votes += 1                     # Add 1 vote to the total votes counted  
        if candidate.get(Candidate) == None: # This looks up the candidate in the dictitonary.  If None returned, they are not in it
                candidate[Candidate] = 1     # This adds the candidate to the dictionary, and initializes them with their first vote
        else: candidate[Candidate] += 1      # Since we had a valid return, we use their name as a key, and add 1 to their vote total    

# ------------------------------
# --- Finish and Output Data ---
# ------------------------------

# Sort the dictionary by the votes in descending order (reverse=True) and put in sorted_by_votes
sorted_by_votes = sorted(candidate.items(), key= lambda vote_count: vote_count[1], reverse=True)

######## Test Print Block #########
# print(f'candidate list and votes = {candidate}')
# print(f'sorted by votes= {sorted_by_votes}')
######## Test Print Block #########

Winner = list(candidate.keys())[0]

# Print to Terminal
print(f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_Votes:,}\n"
    f"----------------------------")
for x in sorted_by_votes:
    print(f"{x[0]}:  {float(100*(x[1]/Total_Votes)):.3f}% ({x[1]:,})")
print(f"----------------------------\n"
    f"Winner: {Winner}\n"
    f"----------------------------")


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