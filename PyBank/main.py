# --------------------------------------------
# --- Python Challenge - PyBank            ---
#---------------------------------------------

# --------------------------------------------
# INITIALIZATION
# --------------------------------------------
# import libraries
import os, csv

# Initialize variables for the Analysis
Total_Months = 0                    # Count of the Number of months in the analysis
Total_Profit_Loss = 0               # Sum of the Profit / Loss for each of the months

Greatest_Increase_Amt = 0           # Largest Profit over the entire period of analysis 
Greatest_Increase_Date = "MMM-YYYY" # Date when the Largest Profit occured during the entire period of analysis

Greatest_Decrease_Amt = 0           # Largest Loss over the entire period of analysis 
Greatest_Decrease_Date = "MMM-YYYY" # Date when the Largest Loss occured during the entire period of analysis

# -----------------------------------
# --- Setup Input File Processing ---
# -----------------------------------

# Set Path to the data file in the Resources folder
BankData_csv_path = os.path.join('Resources', 'budget_data.csv')

# Open the data file with Read capabilities
with open(BankData_csv_path, 'r') as csvfilein:

    # Read the data, and since it is a CSV, Split the data on comma delimiters
    BankData_row = csv.reader(csvfilein, delimiter=',')

    # Store the initial header line
    BankData_Header = next(BankData_row)

# -----------------------------------
# --- Main Processing Loop        ---
# -----------------------------------
    # Loop through the data 
    for row in BankData_row:

        # Read the Profit_loss and Entry_date for the current row for readability of the code below
        Profit_Loss_Amt =  int(row[1])
        Entry_Date = row[0]
        
        # Read Each set of data and calculate running numbers
        Total_Months += 1                    # Find the total number of months, which is the count of entries
        Total_Profit_Loss += Profit_Loss_Amt # Find the net total amount of "Profit/Losses" over the period by adding each entry

        # Look to see if the current entry is a greater increase or decrease
        if  Profit_Loss_Amt > Greatest_Increase_Amt:
            Greatest_Increase_Amt =  Profit_Loss_Amt
            Greatest_Increase_Date = Entry_Date
        elif Profit_Loss_Amt < Greatest_Decrease_Amt:
            Greatest_Decrease_Amt =  Profit_Loss_Amt
            Greatest_Decrease_Date = Entry_Date
  
# ------------------------------
# --- Finish and Output Data ---
# ------------------------------
# Print to Terminal
print(f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Total_Profit_Loss:,}\n"
    f"Average Change: ${float(Total_Profit_Loss/Total_Months):,.2f}\n"
    f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_Amt:,})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease_Amt:,})")

# Set Path to the output file in the analysis folder
BankDataAnalysis_csv_path = os.path.join('analysis', 'budget_data_analysis.csv')

# Open the data file with write capabilities
with open(BankDataAnalysis_csv_path, 'w',newline="") as csvfileout:
     csvwriter = csv.writer(csvfileout, delimiter=',')
     csvwriter.writerow(["Financial Analysis"])
     csvwriter.writerow(["----------------------------"])
     csvwriter.writerow([f"Total Months: {Total_Months}"])
     csvwriter.writerow([f"Total: ${Total_Profit_Loss:,}"])
     csvwriter.writerow([f"Average Change: ${float(Total_Profit_Loss/Total_Months):,.2f}"])
     csvwriter.writerow([f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_Amt:,})"])
     csvwriter.writerow([f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease_Amt:,})"])