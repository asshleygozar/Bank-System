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
        deposit = int(input("Please enter initial deposit: "))

        info = {"account-number":account_number, "pin":pin, "balance": deposit}
        account.append(info)

        try:
            with open(file_path, "w") as file:
                json.dump(account, file, indent=2)
        except FileNotFoundError:
            account = []
            print("File not found!")
    except ValueError:
        print("Integer Only!")
    log_in(accounts)

def log_in(accounts):
    try:
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        for account in accounts:
            if account["account-number"] == account_number and account["pin"] == pin:
                print("Log In Successful!")
                transactions()
            else:
                print("Invalid Account Number or Pin")

    except ValueError:
        print("Integer Input Only!")

def transactions():
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
                    deposit(accounts)
                    break
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    break
                case _:
                    print("Invalid Input!")
        except ValueError:
            print("Integer Only!")
def deposit(accounts):
    try:
        amount = int(input("Enter amount to deposit here: "))
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your pin for confirmation: "))

        for account in accounts:
            if account["account-number"] == account_number and account["pin"] == pin:
               total_amount = account["balance"] + amount
               account["balance"] = total_amount
               try:
                   with open(file_path, "w") as file:
                       json.dump(accounts,file, indent=3)
               except FileNotFoundError:
                   print("File not Found!")
               print("Deposit Successful!")
    except ValueError:
        print("Integer Only!")

create_account(accounts)