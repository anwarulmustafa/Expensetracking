from datetime import datetime
#main fuction for reading a file

def addexpenses():
    while True:
        try:
            date_str = input("Enter into the date [yyyy-MM-DD]:")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid Date!")

    description = input("Enter the expense description : ")
    while True:
        try:
            amount = float(input("Enter the spent Amount: "))
            break
        except ValueError:
            print("Please enter a valid amount!")
    #check if the amount is float

    with open("expenses.txt","a") as expensefile:
        expensefile.write(f"{date}|{description}|{amount}\n")
        print("Expense Enter successfully!")
#function to view the expenses
def viewexpenses():
    try:
        with open("expenses.txt", "r") as expensefile:
            myexpenses = expensefile.readlines()
            if not myexpenses:
                print("There is no expense to display!")
                return
            print("Date | Description | Amount")
            print("-" * 40)
            for expense in myexpenses:
                print(expense.strip())
    except FileNotFoundError:
        print("There is no file!")
#---------------------------------
#function to calculate the amount

def calculate_amount():
    try:
        totalex = 0
        with open("expenses.txt","r") as expensefile:
            expenses = expensefile.readlines()
            if not expenses:
                print("There is no expense to read!")
                return
            for expense in expenses:
                exline = expense.split("|")
                totalex += float(exline[2])
            print(f"Total Amount Spent ${totalex}")
    except FileNotFoundError:
        print("File did't found!")

#-------------------------------
#main fuction to run the program
def main():
    while True:
        print("\n---Expenses Traking Project---")
        print("1. Add Expense\n")
        print("2.View Expenses\n")
        print("3. Calculate Total\n")
        print("4.Exit\n")
        choice = input("Enter your choice (1-4)")
        #code to select a number from 1
        if choice == '1':
            addexpenses()
        elif choice == '2':
            viewexpenses()
        elif choice == '3':
            calculate_amount()
        elif choice == '4':
            print("Exiting Expense Tracking. Goodbye")
            break
        else:
            print("Invali choice! Try again!")

main()
