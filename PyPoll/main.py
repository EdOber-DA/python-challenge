# --------------------------------------------
# --- Python Challenge - PyBank            ---
#---------------------------------------------

# --------------------------------------------
# INITIALIZATION
# --------------------------------------------
# import libraries
import os, csv

# Initialize variables for the Analysis
candidate = {}        # Initialize and empty set that will be updated to contain the candidate names and vote counters
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
        Voter_ID = row[0]       # for future use
        County = row[1]         # for future use
        Candidate = row[2]      # will be used in the dictionary lookup

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

# ------------------------------
# --- Print to the terminal  ---
# ------------------------------

# Print the headers
print(f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_Votes:,}\n"
    f"----------------------------")

# Loop through the candidates and print a nice formatted summary
for x in sorted_by_votes:
    namejust = (x[0]+":").ljust(10)
    print(f"{namejust:10} {float(100*(x[1]/Total_Votes)):6.3f}%  ({x[1]:,})")

# Print the trailer with the winner
print(f"----------------------------\n"
    f"Winner: {sorted_by_votes[0][0]}\n"    # the first entry, first part is the winner's name
    f"----------------------------")

# ------------------------------
# --- Print to the file      ---
# ------------------------------

# Set Path to the output file in the analysis folder
PollDataAnalysis_csv_path = os.path.join('analysis', 'poll_data_analysis.csv')

# Open the data file with write capabilities
with open(PollDataAnalysis_csv_path, 'w',newline="") as csvfileout:
    csvwriter = csv.writer(csvfileout, delimiter=',')

# Print the headers
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {Total_Votes:,}"])
    csvwriter.writerow(["----------------------------"])

#   Loop through the candidates and print a nice formatted summary
    for x in sorted_by_votes:
        namejust = (x[0]+":").ljust(10)
        csvwriter.writerow([f"{namejust:10} {float(100*(x[1]/Total_Votes)):6.3f}%  ({x[1]:,})"])

# Print the trailer with the winner
    csvwriter.writerow([f"----------------------------"])
    csvwriter.writerow([f"Winner: {sorted_by_votes[0][0]}"])    # the first entry, first part is the winner's name
    csvwriter.writerow([f"----------------------------"])