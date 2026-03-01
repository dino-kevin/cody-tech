expenses_list = []

def menu(choice:int):
    if choice == 0:
        print("Welcome to the Daily Expense Tracker!")
    print("")
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")

def select_option(choice: int, expenses_list: list):
    match(choice):
        case 1:
            new_expense = float(input())
            if new_expense:
                expenses_list.append(new_expense)
                print("Expense added successfully!")
            else: 
                print("No expenses recorded yet.")
        case 2:
            if expenses_list:
                print("Your expenses:")
                for i, expense in enumerate(expenses_list, start=1):
                    print(f"{i}. {expense}")
            else: 
                print("No expenses recorded yet.")
        case 3:
            if expenses_list:
                print(f"Total expense: {sum(expenses_list)}")
                print(f"Average expense: {sum(expenses_list)/len(expenses_list)}")
            else:
                print("No expenses recorded yet.")
        case 4:
            expenses_list.clear()
            print("All expenses cleared.")
        case 5:
            print("Exiting the Daily Expense Tracker. Goodbye!")
        case _:
            print("Invalid choice. Please try again.")

choice = 0
while choice != 5:
    menu(choice)
    choice = int(input())
    if choice > 0:
        select_option(choice, expenses_list)
    else:
        print("Invalid choice. Please try again.")