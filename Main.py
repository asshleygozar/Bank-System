import sys
import random
from Database import BankDatabase

class BankSystem:

    def __init__(self):
        pass
        
    def transactions(self):

        while True:

            print("Choose your Transaction: ")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            try:
                choice = int(input("Enter here: "))
                match choice:
                    case 1:
                        BankSystem.deposit(self)
                        break
                    case 2:
                        BankSystem.withdraw(self)
                        break
                    case 3:
                        BankSystem.check_balance(self)
                        break
                    case 4:
                        sys.exit(0)
                    case _:
                        print("Invalid Input!")
            except ValueError:
                print("Integer Only!")

    def log_in(self):

            try:
                while True:
                    account_number = int(input("Enter your account number: "))
                    pin = int(input("Enter your pin: "))
                    
                    if len(str(pin)) > 4:
                        print("4 digits of pin only!")
                    else:
                        BankDatabase.BankDatabase.log_in_validation(self,account_number,pin)
                        BankSystem.transactions(self)
                        break
            except ValueError:
                print("Integer Input Only!")

    def create_account(self):

        try:
            account_number = random.randint(100000,999999)
            pin = int(input("Create your pin(4 digits only!): "))
            
            if len(str(pin)) > 4:
                print("4 digits of pin only!")
            else:
                deposit = int(input("Please enter initial deposit: "))
                BankDatabase.BankDatabase.create_account(account_number,pin,deposit)
                print("Account created successfully!")
                print(f"Here is you Account Number: {account_number}")
                print(f"Here is your pin: {pin}")
                BankSystem.action(self)

        except ValueError:
            
            print("Integer Only!")
            
    
    def action(self):

        try:
            while True:
                print("Choose Action")
                print("1. Create Account")
                print("2. Log In")
                print("3. Exit")
                choice = int(input("Enter here: "))
                match choice:
                    case 1:
                        BankSystem.create_account()
                        break
                    case 2:
                        BankSystem.log_in(self)
                        break
                    case 3:
                        break
                    case _:
                        print("Invalid Input!")
        except ValueError:
            print("Integer Number Only!")

    def deposit(self):

        try:
            deposit_money = int(input("Enter amount to deposit: "))
            BankDatabase.BankDatabase.deposit(self, deposit_money)

        except ValueError:
            print("Integer Only!")

    def withdraw(self):

        try:
            withdraw_money = int(input("Enter amount to withdraw: "))
            BankDatabase.BankDatabase.withdraw(self, withdraw_money)

        except ValueError:
            print("Integer Only!")
    
    def check_balance(self):
        BankDatabase.BankDatabase.balance(self)

    def changePin():
        pass
       
bank = BankSystem()
bank.action()