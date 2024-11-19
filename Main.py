import json
import sys
import random
class BankSystem:

    def __init__(self):
        self.file_path = "Database\\accounts.json"
        self.accounts = BankSystem.load_accounts()
        self.__temp_hold_accountnumber = 0 

    def get_hold_data(self):
       return self.__temp_hold_accountnumber
    
    def set_hold_data(self, account_number):
        self.__temp_hold_accountnumber = account_number

    def load_accounts(file_path = "Database\\accounts.json"):
        try:
            with open(file_path, "r") as file:
                accounts = json.load(file)
        except FileNotFoundError:
            accounts = []
        except json.JSONDecodeError:
            accounts = []
            print("Error loading file, Starting with empty list")
        return accounts
        
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
                    case 3:
                        BankSystem.check_balance(self, self.accounts)
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
    def create_account(self,account):
        try:
            account_number = random.randint(100000,999999)
            pin = int(input("Create your pin(4 digits only!): "))
            deposit = int(input("Please enter initial deposit: "))
            print(f"Here is you Account Number: {account_number}")
            print(f"Here is your pin: {pin}")

            info = {"account-number":account_number, "pin":pin, "balance": deposit}
            account.append(info)

            try:
                with open(self.file_path, "w") as file:
                    json.dump(account, file, indent=2)
            except FileNotFoundError:
                account = []
                print("File not found!")
        except ValueError:
            print("Integer Only!")
        BankSystem.log_in(self.accounts)

    
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
                        BankSystem.create_account(self.accounts)
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