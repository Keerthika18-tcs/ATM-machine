
balance=100
PIN="4321"  
def pin():    
    attempts=3  
    while attempts > 0:
        entered_pin=input("Enter your 4-digit PIN: ")
        if entered_pin==PIN:
            print("pin successful.\n")
            return True
        else:
            attempts-= 1
            print(f"Incorrect PIN. You have {attempts} attempt(s) left.")   
    print("Too many incorrect attempts. Exiting the system.")
    return False
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} has been deposited successfully.")
        check_balance()
    else:
        print("Invalid deposit amount. Please enter a positive amount.")
def withdraw(amount):
    global balance
    if amount > 0:
        if amount<= balance:
            balance -= amount
            print(f"${amount:.2f} has been withdrawn successfully.")
            check_balance()
        else:
            print("Insufficient funds. Please try a smaller amount.")
    else:
        print("Invalid withdrawal amount. Please enter a positive amount.")
def menu():
    """Display the ATM menu and prompt user for an action."""
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
if pin():
    menu()
    
