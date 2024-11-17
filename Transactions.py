import json
import random


file_path = "Database/accounts.json"

def load_accounts(file_path = "Database/accounts.json"):
    try:
        with open(file_path, "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = []
    except json.JSONDecodeError:
        print("Error Reading Contacts! Starting with empty lists")
        accounts = []
    
    return accounts


def choose_action():
    while True:
        print("Choose Transaction: ")
        print("1. Create a Bank Account")
        print("2. Log In")
        print("3. Exit")
        try:
            choice = int(input("Enter here: "))
            match choice:
                case 1:
                    create_bank_account(accounts)
                    break
                case 2:
                    log_In()
                case 3:
                    break
                case _:
                    print("Invalid Input!")
        except ValueError:
            print("Integer Value Only!")
    
def choose_transaction():
    while True:
        print("Choose Transaction: ")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check the account balance")
        print("4. Exit")
        try:
            choice = int(input("Enter here: "))
            match choice:
                case 1:
                    deposit_money()
                case 2:
                    withdraw_money()
                case 3:
                    check_balance()
                case 4:
                    print("Bye Bye1")
                case _:
                    print("Invalid Input!")

        except ValueError:
            print("Number Only!")

def create_bank_account(accounts):
    accounts = []
    pin = int(input("Create your Pin: "))
    account_number = random.randint(100000,900000)

    details = {"accountnumber": account_number, "pin":pin}
    
    accounts.append(details)
    
    try:
        with open("Database/accounts.json", "a") as file:
            json.dump(details, file, indent=2)
            choose_action()

    except FileNotFoundError:
        print("File Not Found!")
    except IOError:
        print("Error saving input!")
    except ValueError:
        print("Invalid Input!")
        
            
        
def log_In(accounts):
    account_number = input("Enter your Account Number: ")
    pin = int(input("Enter you pin (4 digits): "))

    for account in accounts:
        if account["account_number"] == account_number:
            if account["account_number"] and account["pin"] == account_number and pin:
                choose_transaction()
            else:
                print("Account Number and Pin does not match!")
        else:
            print("Account Number does not exists!")
            break

def deposit_money():
    pass

def withdraw_money():
    pass

def check_balance():
    pass
accounts = load_accounts()
create_bank_account(accounts)
