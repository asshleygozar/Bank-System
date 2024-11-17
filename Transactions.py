from Main import Main
import json
import random

file_path = "JsonFiles/accounts.json"

def load_accounts(file_path = "JsonFiles/accounts.json"):
    try:
        with open(file_path, "r") as file:
           accounts = json.load(file)
    except FileNotFoundError:
        print("File Not Found!")
        accounts = []
    except json.JSONDecodeError:
        print("Error Reading Contacts!")
        accounts = []
    return accounts

accounts = load_accounts(file_path)

def create_bank_account(accounts):

    while True:
        try:
            name = input("Enter your name: ")
            birthday = input("MM/dd/YYYY")
            
            for account in accounts:
                if name and birthday == account:
                    print("You already have an account!")
                    print("Log in Instead!")
                    log_In()
                    break
                else:
                    account_number = random.randint(100000)
                    details = {"name": name, "birthday": birthday, "account_number:": account_number}
                    try:
                        with open(file_path, "a") as file:
                            accounts.append(details)
                            Main.choose_transaction()
                    except FileNotFoundError:
                        print("File Not Found!")
                    pass
        except ValueError:
            print("Please follow the format!")
        



def log_In():
    pass

def deposit_money():
    pass

def withdraw_money():
    pass

def check_balance():
    pass
