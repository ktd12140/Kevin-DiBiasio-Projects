"""Bank Account Management- Foundations of Programming Kevin DiBiasio"""


class BankAccount: #Creates the class BankAccount
    def __init__(self,account_number,balance): #Creates an instance of the class BankAccount
        self.account_number = account_number #instance variable
        self.balance = balance #instance variable

    def check_balance(self): #Creates a method to display Bank Account information
        return self.balance #Returns the balance in the users account

    def bank_details(self): #Creates a method to display account details
        print("Your account number is", self.account_number) #Displays the user's account number to them

    def deposit(self, amount): #Creates a method to return the balance of the user's account after a deposit
        self.balance += amount #Takes the initial balance and adds it to the deposit amount
        return self.balance #Returns the new balance after the the deposit

    def withdraw(self, amount):#Creates a method to return the balance of the user's account after a withdrawal
        if self.balance >= amount: #Checks if the balance in the user's account is greater or equal to the amount they want to withdraw.
            self.balance -= amount #When the balance is greater than the amount withdrawn the amount will be subtracted from the account.
            return True
        else: #Checks all other scenarios including if the balance in the user's account is less than the amount they want to withdraw.
            print("Insufficient balance.") #Displays to the user that there is insufficient funds in their account to withdraw the amount they want.
            return False


class Bank: #Creates the class Bank that inherits from the parent class BankAccount 
    def __init__(self): #Creates an instance of the class Bank
        self.accounts = {} #Creates an empty dictionary called accounts
        
    def create_account(self): #Creates a method to have the user create their account number
        account_number = len(self.accounts) + 1 #Sets the variable account_number equal to the length of the accounts dictionary.
        balance = float(input("Enter initial balance: ")) #Asks the user to enter an initial balance to their account.
        account = BankAccount(account_number, balance) # Creates an instance of the BankAccount class that will be stored in the variable account.
        self.accounts[account_number] = account # Creates a key value pair in the accounts dictionary
        print(f"Account created with Account Number: {account_number}") #Displays the account number to the user 

    def get_account(self,account_number): #Creates a method to get an account
        return self.accounts.get(account_number) #returns account details

    def deposit(self,account_number,amount): #Creates a method for the user to deposit money into their account
        account = self.get_account(account_number) #Calls get_account method to run and stores the result in the variable account.
        if account: 
            account.deposit(amount) #Calls the method deposit in the BankAccount class to deposit money into account.
            print('Deposited ',amount, 'into account number ',account_number) #Displays the amount of money deposited into the selected account to the user.
        else:
            print('Account not found try again') #Displays no account found if the user enters an invalid account number

    
    def withdraw(self, account_number, amount): #Creates a method for the user to withdraw money from their account
        account = self.get_account(account_number) #Calls get_account method to run and stores the result in the variable account.
        if account:
            if account.withdraw(amount): #Calls the method withdraw in the BankAccount class to withdraw money from account.
                print('Withdrew ',amount, 'from account number ',account_number) #Displays the amount of money withdrawn from the selected account to the user.
        else:
            print("Account not found try again.")#Displays no account found if the user enters an invalid account number

    
    def transfer(self, from_account_number, to_account_number, amount): #Creates a method for the user to transfer money between any two accounts.
        from_account = self.get_account(from_account_number) #Calls get_account method to run and stores the result in the variable from_account.
        to_account = self.get_account(to_account_number) #Calls get_account method to run and stores the result in the variable to_account.
        if from_account and to_account:#Checks if the two accounts are the from_account and to_account accounts
            if from_account.withdraw(amount): #Checks if the withdrawn amount is from the from_account account
                to_account.deposit(amount) #If the withdrawn amount is from the from_account it will be deposited into to_account.
                print(f"Transferred {amount} from Account {from_account_number} to Account {to_account_number}") #Dispalys transfer to user.
        else: #Checks for nonexistent accounts
            print("One or both accounts not found.") #Displays to the user that they entered invalid account numbers.


def menu(): #Creates a function to display menu items for the user to choose from.
    print("Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. Quit")

def execute_choice(bank): #Creates a function to execute menu actions
    try:
        choice = int(input("Enter your choice: ")) #Asks the user to enter the number of the menu choice they wish to have executed.
        if choice == 1: #Checks if the user entered menu choice 1
            bank.create_account() #Calls upon the method create_account method in the Bank class to create accounts for the user.
        elif choice == 2: #Checks if the user entered menu choice 2
            account_number = int(input('Enter account number: ')) #Asks the user to enter an account number they want to deposit money into.
            amount = float(input("Enter amount to deposit: ")) #Asks the user to enter the amount they want to deposit into the selected account.
            bank.deposit(account_number,amount) #Calls upon the deposit method in the Bank class to deposit money into the selected account.
        elif choice == 3: #Checks if the user entered menu choice 3
            account_number = int(input('Enter account number: ')) #Asks the user to enter an account number they want to withdraw money from.
            amount = float(input('Enter amount to withdraw: ')) #Asks the user to enter the amount they want to withdraw from the selected account.
            bank.withdraw(account_number, amount) #Calls upon the withdraw method in the Bank class to withdraw money from the selected account.
        elif choice == 4: #Checks if the user entered menu choice 4
            account_number = int(input("Enter Account Number: ")) #Asks the user to enter an account number they want to check the balance for.
            account = bank.get_account(account_number) # Calls upon the get_account method from the Bank class to get the account.
            if account:
                print(f"Balance for Account {account_number}: {account.check_balance()}") #Displays the balance in the selected account
            else:
                print("Account not found.") #Displays to the user that they entered an invalid account number.
        elif choice == 5: #Checks if the user entered menu choice 5
            from_account_number = int(input("Enter Account Number to transfer from: ")) #Asks the user to enter the account number to transfer money from
            to_account_number = int(input("Enter Account Number to transfer to: ")) #Asks the user to enter the account number to transfer money to
            amount = float(input("Enter amount to transfer: ")) #Asks the user to enter the amount they want to transfer
            bank.transfer(from_account_number, to_account_number, amount) # Calls upon the transfer method in the bank class to transfer money from one account to the other.
        elif choice == 6:#Checks if the user entered menu choice 6
            print("Goodbye!") #displays goodbye to the user when they exit the program.
            return
        else:
            print("Invalid choice.") #displays to the user when they enter an invalid menu choice
    except ValueError: #exception raised when a user input would cause a ValueError.
        print('invalid input. Try again') #displays to the user when the user enters an invalid choice.

    continue_operation(bank) #Performs the continue operation function.


def continue_operation(bank): #Creates the function continue_operation
    while True: #Start a loop to continually ask user for entries if they enter an invalid input.
        choice = input("Do you want to continue? (y/n): ") #Asks user to enter if they want to continue with the program or not.
        if choice.lower() == 'y': #Checks if the user entered y to continue the program  
            execute_choice(bank) #When the user enters y, the execute_function will be activated again.
            break #Breaks the while loop 
        elif choice.lower() == 'n': #Checks if the user entered n to end the program
            print('Goodbye!') #displays goodbye to the user when they exit the program.
            break #Breaks the while loop
        else:
            print('Invalid input. Try again') #Continually displayed to the user if they enter an invalid input (not y or n)

bank = Bank() #Creates an instance of the Bank class
menu() #Executes the menu function to display the menu to the user
execute_choice(bank) #Executes menu options
