# Dependencies
import csv
import os

# Files to load and output
Input_file = 'Resources/budget_data.csv'
txt_output = 'Analysis/outcome.txt'

# Assign variable names and set initial values to zero
# The total number of months included in the dataset is stated below
Total_months = 0
# The amount change for each month is stated below
last_amount = 0
# Empty list as shown below
month_change =[]
# amount_list is also an empty list that matches to the month of change
# as shown below
amount_change_list =[]
# variable that define the greatest increase as shown below in ascending
greatest_increase =["", 0]
# variable that defines the greatest decrease as shown below in descending
greatest_decrease =["", 9999999999999999]
# keeps track of the total amount as the loop code runs 
Total_amount = 0

#Read csv file and convert to list of dictionaries
with open(Input_file) as main_data:
    csv_reader = csv.DictReader(main_data)
    # Then read each row of the dictionary
    for row in csv_reader:

        #track the total variables assigned above
        Total_months = Total_months + 1 
        Total_amount = Total_amount + int(row["Profit/Losses"])

        #track the change in amount
        amount_change = int(row["Profit/Losses"]) - last_amount
        last_amount = int(row["Profit/Losses"])
        amount_change_list = amount_change_list + [amount_change]
        month_change = month_change + [row["Date"]]

        #Calculate the greatest increase
        if (amount_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = amount_change

        #Calculate the greatest decrease 
        if (amount_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = amount_change

    #Calculate the average change in amount
    amount_average =sum(amount_change_list) / len(amount_change_list)

    #Output Summary
    output = (
        f"\nFianical Analysis\n"
        f'--------------------\n'
        f'Total Months: {Total_months}\n'
        f'Total: ${Total_amount}\n'
        f'Average Change: ${amount_average}\n'
        f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
        f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
    )
    
# Print the output in terminal
print(output)

# Export output to txt
with open(txt_output, 'w') as txt_file:
    txt_file.write(output)
    
