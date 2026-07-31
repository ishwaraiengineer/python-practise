
# BANK MANAGEMENT SYSTEM


accounts = {}

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:
            print("Account already exists!")

        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            accounts[acc_no] = {
                "name": name,
                "balance": balance
            }

            print("Account Created Successfully!")

    
    elif choice == "2":

        if not accounts:
            print("No accounts found!")

        else:
            print("\n===== ACCOUNT DETAILS =====")

            for acc_no, details in accounts.items():

                print(f"""
Account Number : {acc_no}
Name           : {details['name']}
Balance        : ₹{details['balance']}
""")

    elif choice == "3":

        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:

            details = accounts[acc_no]

            print("\n ACCOUNT FOUND ")
            print("Name    :", details["name"])
            print("Balance : ₹", details["balance"])

        else:
            print("Account not found!")


    elif choice == "4":

        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:

            amount = float(input("Enter Deposit Amount: "))

            accounts[acc_no]["balance"] += amount

            print("Money Deposited Successfully!")
            print("Updated Balance : ₹", accounts[acc_no]["balance"])

        else:
            print("Account not found!")


    elif choice == "5":

        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= accounts[acc_no]["balance"]:

                accounts[acc_no]["balance"] -= amount

                print("Withdrawal Successful!")
                print("Remaining Balance : ₹", accounts[acc_no]["balance"])

            else:
                print("Insufficient Balance!")

        else:
            print("Account not found!")


    elif choice == "6":

        acc_no = int(input("Enter Account Number to Delete: "))

        if acc_no in accounts:

            del accounts[acc_no]

            print("Account Deleted Successfully!")

        else:
            print("Account not found!")

    
    elif choice == "7":

        print("Thank You For Using Bank Management System")
        break

    else:
        print("Invalid Choice!")