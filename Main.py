import json
import sys
import random
from Database import BankDatabase


class BankSystem:

    def __init__(self):
        self.__temp_hold_accountnumber = 0 
        
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
                        BankSystem.deposit(self,self.accounts)
                        break
                    case 2:
                        BankSystem.withdraw(self,self.accounts)
                        break
                    case 3:
                        BankSystem.check_balance(self, self.accounts)
                        break
                    case 4:
                        sys.exit(0)
                    case _:
                        print("Invalid Input!")
            except ValueError:
                print("Integer Only!")

    def log_in(self,accounts):

            try:
                while True:
                    account_number = int(input("Enter your account number: "))
                    pin = int(input("Enter your pin: "))

                    for account in accounts:
                        if account["account-number"] == account_number and account["pin"] == pin:
                            BankSystem.set_hold_data(self,account["account-number"])
                            print("Log In Successful!")
                            BankSystem.transactions(self)
                            break
                    print("Invalid Account Number or Pin")
            except ValueError:
                print("Integer Input Only!")

    def create_account():

        try:
            account_number = random.randint(100000,999999)
            pin = int(input("Create your pin(4 digits only!): "))
            
            if len(str(pin)) > 4:
                print("4 digits of pin only!")
            else:
                deposit = int(input("Please enter initial deposit: "))
                BankDatabase.BankDatabase.create_account(account_number,pin,deposit)
                print(f"Here is you Account Number: {account_number}")
                print(f"Here is your pin: {pin}")

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
                    case 2:
                        BankSystem.log_in(self,self.accounts)
                    case 3:
                        break
                    case _:
                        print("Invalid Input!")
        except ValueError:
            print("Integer Number Only!")


    def deposit(self,accounts):

        try:
            deposit_money = int(input("Enter amount to deposit here: "))
            
            for account in accounts:
               if account["account-number"] == BankSystem.get_hold_data(self):
                    while True:
                        pin = int(input("Enter your pin for confirmation: "))
                        if account["pin"] == pin:
                            account["balance"] = account["balance"] + deposit_money
                            try:
                                with open(self.file_path, "w") as file:
                                    json.dump(accounts, file, indent=3)
                            except FileNotFoundError:
                                print("File not Found!")
                            BankSystem.transactions(self)
                            break
                        else:
                            print("Incorrect Pin!")
        except ValueError:
            print("Integer Only!")

    def withdraw(self,accounts):

        while True:
            try:
                withdraw_money = int(input("Enter amount to withdraw here: "))
                for account in accounts:
                    if account["account-number"] == BankSystem.get_hold_data(self):
                        if withdraw_money > account["balance"]:
                            print("Insufficient Balance!")
                        else:
                            while True:
                                pin = int(input("Enter your pin for confirmation: "))
                                if account["pin"] == pin:
                                    account["balance"] = account["balance"] - withdraw_money
                                    try:
                                        with open(self.file_path, "w") as file:
                                            json.dump(accounts, file, indent=3)
                                    except FileNotFoundError:
                                        print("File not Found!")
                                    BankSystem.transactions(self)
                                    break
                                else:
                                    print("Invalid Pin! Try Again")
            except ValueError:
                print("Integer Number Only!")
    
    def check_balance(self,accounts):
        for account in accounts:
            if account["account-number"] == BankSystem.get_hold_data(self):
                print(f"Remaining Balance: {account["balance"]}")
                break
                BankSystem.transactions(self)
       
bank = BankSystem()
bank.action()