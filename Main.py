import json
import random
class BankSystem:

    def __init__(self):
        self.file_path = "Database\\accounts.json"
        self.accounts = BankSystem.load_accounts()
        self.temp_hold_account_number = 0

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
                        pass
                    case 4:
                        break
                    case _:
                        print("Invalid Input!")
            except ValueError:
                print("Integer Only!")
    def log_in(self,accounts):
            try:
                account_number = int(input("Enter your account number: "))
                pin = int(input("Enter your pin: "))

                for account in accounts:
                    if account["account-number"] == account_number and account["pin"] == pin:
                        self.temp_hold_account_number = account["account-number"]
                        print("Log In Successful!")
                        BankSystem.transactions(self)
                    else:
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
            amount = int(input("Enter amount to deposit here: "))
            pin = int(input("Enter your pin for confirmation: "))
            
            for account in accounts:
                if account["pin"] == pin and account["account-number"] == self.temp_hold_account_number:
                    total_amount = account["balance"] + amount
                    account["balance"] = total_amount
                    try:
                        with open(self.file_path, "w") as file:
                            json.dump(accounts,file, indent=3)
                    except FileNotFoundError:
                        print("File not Found!")
                    print("Deposit Successful!")
                else:
                    print("Incorrect Pin!")
        except ValueError:
            print("Integer Only!")
    def withdraw(self,accounts):
        try:
            withdraw_money = int(input("Enter amount to withdraw here: "))
            pin = int(input("Enter your pin for confirmation: "))

            for account in accounts:
                if account["account-number"] == self.temp_hold_account_number and account["pin"] == pin:
                    if withdraw_money > account["balance"]:
                        print("Insufficient Balance!")
                    else:
                        total_amount = account["balance"] - withdraw_money
                        account["balance"] = total_amount
                        try:
                            with open(self.file_path, "w") as file:
                                json.dump(accounts, file, indent=3)
                        except FileNotFoundError:
                            print("File not found!")
                    print("Transaction Successful!")
                    BankSystem.transactions(self)
        except ValueError:
            print("Integer Number Only!")
    
bank = BankSystem()
bank.action()