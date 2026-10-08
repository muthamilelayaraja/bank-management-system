import json
import os

FILE_NAME = "bank_data.json"


# Load accounts from file
def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Save accounts to file
def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# Create a new account
def create_account(accounts):
    account_no = input("Enter account number: ")

    if account_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    phone = input("Enter phone number: ")
    initial_deposit = float(input("Enter initial deposit: "))

    if initial_deposit < 0:
        print("Deposit cannot be negative.")
        return

    accounts[account_no] = {
        "name": name,
        "phone": phone,
        "balance": initial_deposit
    }

    save_accounts(accounts)
    print("Account created successfully!")


# Deposit money
def deposit(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    accounts[account_no]["balance"] += amount
    save_accounts(accounts)

    print(f"₹{amount:.2f} deposited successfully.")
    print(f"Current balance: ₹{accounts[account_no]['balance']:.2f}")


# Withdraw money
def withdraw(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    if amount > accounts[account_no]["balance"]:
        print("Insufficient balance!")
        return

    accounts[account_no]["balance"] -= amount
    save_accounts(accounts)

    print(f"₹{amount:.2f} withdrawn successfully.")
    print(f"Current balance: ₹{accounts[account_no]['balance']:.2f}")


# Check balance
def check_balance(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    print(f"Account Holder: {accounts[account_no]['name']}")
    print(f"Balance: ₹{accounts[account_no]['balance']:.2f}")


# Display account details
def account_details(accounts):
    account_no = input("Enter account number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    print("\n----- Account Details -----")
    print(f"Account Number : {account_no}")
    print(f"Account Holder : {account['name']}")
    print(f"Phone Number   : {account['phone']}")
    print(f"Balance        : ₹{account['balance']:.2f}")


# Main program
def main():
    accounts = load_accounts()

    while True:
        print("\n========== BANK MANAGEMENT SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. Exit")
        print("============================================")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                create_account(accounts)

            elif choice == "2":
                deposit(accounts)

            elif choice == "3":
                withdraw(accounts)

            elif choice == "4":
                check_balance(accounts)

            elif choice == "5":
                account_details(accounts)

            elif choice == "6":
                print("Thank you for using the Bank Management System!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
