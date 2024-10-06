# ATM Interface by the use of python program

def verify_account_number():

    account_number = input("Enter the account number: ")
    last_four_digits = account_number[-4:]
    user_input=input("Enter the last four digits of the account number:  ")

    if user_input == last_four_digits:

        print("Verification Successful!")

    else:

        print("Verification failed! Try again")


def show_balance(balance):

    print(f"Current balance: ₹{balance:.2f}")

def deposit():

    amount = float(input("Enter an amount: ₹"))

    if amount<0:

        print("Invalid Amount")
        return 0

    else:

        return amount    


def withdraw(balance):

    amount = float(input("Enter an amount: ₹"))

    if amount > balance:

        print("Insufficient funds")
        return 0

    elif amount < 0:

        print("Invalid Amount")
        return 0

    else:
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:

        print("Dear customer, Welcome to the Coder ATM")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter the option: ")

        if choice == '1':

            show_balance(balance)

        elif choice == '2':

            balance += deposit()

        elif choice == '3':

            balance -= withdraw(balance)

        elif choice == '4':

            is_running = False

        else:

            print("Invalid option")  

    print("Thank you for using Coder ATM")

if __name__=="__main__":

   verify_account_number() 

if __name__=="__main__":
    
    main()
