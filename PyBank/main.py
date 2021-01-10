# ???? Calculate the changes in "Profit/Losses" over the entire period ???? (Same as the total??)
#### ADD APPROPRIATE COMMENTS AND Program Headers

# import libraries
import os, csv

# Initialize variables for the Analysis
Total_Months = 0                    # Count of the Number of months in the analysis
Total_Profit_Loss = 0               # Sum of the Profit / Loss for each of the months

Greatest_Increase_Amt = 0               # Largest Profit over the entire period of analysis 
Greatest_Increase_Date = "MMM-YY"   # Date (raw) when the Largest Profit occured during the entire period of analysis

Greatest_Decrease_Amt = 0               # Largest Loss over the entire period of analysis 
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
        # TESTING - reading the data??
        print(f'GIA={Greatest_Increase_Amt},GID={Greatest_Increase_Date},GDA={Greatest_Decrease_Amt}, GDD={Greatest_Decrease_Date}')




# Calculate the changes in "Profit/Loss" and average of the changes

# Calculate the Greatest Increase: (Date and Amount) 

# Calculate the Greatest Decrease: (Date and Amount)