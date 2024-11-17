class Main:

    def choose_transaction():
        while True:
            print("Choose Transaction: ")
            print("1. Create a Bank Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check the account balance")
            print("5. Exit")
            try:
                choice = int(input("Enter here: "))
                match choice:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        print("Bye Bye1")

            except ValueError:
                print("Number Only!")
    choose_transaction()