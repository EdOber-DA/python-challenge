# ???? Calculate the changes in "Profit/Losses" over the entire period ???? (Same as the total??)
#### ADD APPROPRIATE COMMENTS AND Program Headers

# import libraries
import os, csv

# Initialize variables for the Analysis
Total_Months = 0                    # Count of the Number of months in the analysis
Total_Profit_Loss = 0               # Sum of the Profit / Loss for each of the months

Greatest_Increase = 0               # Largest Profit over the entire period of analysis 
Greatest_Increase_Date = "MMM-YY"   # Date (raw) when the Largest Profit occured during the entire period of analysis

Greatest_Decrease = 0               # Largest Loss over the entire period of analysis 
Greatest_Decrease_Date = "MMM-YY"   # Date (raw) when the Largest Loss occured during the entire period of analysis


# Set Path to the data file in the Resources folder
BankData_csv_path = os.path.join('Resources', 'budget_data.csv')

# Open the data file with Read capabilities
with open(BankData_csv_path, 'r') as csvfile:

    # Read the data, and since it is a CSV, Split the data on comma delimiters
    BankData_row = csv.reader(csvfile, delimiter=',')

    # Store the initial header line
    BankData_Header = next(BankData_row)

    # Loop through the data 
    for row in BankData_row:

        # Read Each set of date
        BankData_row_Amount = int(row[1])
        BankData_row_Date = row[0]
        # TESTING - reading the data??
        print(f'Row= {row} and BankData_row_Date = {BankData_row_Date} and BankData_row_Amount= {BankData_row_Amount}')
# Find the total number of months, which is the count of entries

# Find the net total amount of "Profit/Losses" over the period 

# Calculate the changes in "Profit/Loss" and average of the changes

# Calculate the Greatest Increase: (Date and Amount) 

# Calculate the Greatest Decrease: (Date and Amount)