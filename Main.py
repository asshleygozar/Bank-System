import json

file_path = "Database\\accounts.json"

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

accounts = load_accounts()

def create_account(account):
    try:
        account_number = int(input("Enter your account number: "))
        pin = int(input("Create your pin(4 digits only!): "))

        info = {"account-number":account_number, "pin":pin}
        account.append(info)

        try:
            with open(file_path, "w") as file:
                json.dump(account, file, indent=2)
        except FileNotFoundError:
            account = []
            print("File not found!")
    except ValueError:
        print("Integer Only!")
    

create_account(accounts)