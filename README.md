Bank Management System
A simple Bank Management System developed using Python. This application allows users to create bank accounts, deposit and withdraw money, check account balances, and view account details.

Features
Create a new bank account
Deposit money
Withdraw money
Check account balance
View account details
Store account data permanently using a JSON file
Basic input validation
Simple command-line interface
Technologies Used
Python 3
JSON for data storage
File Handling for saving and loading account information
Project Structure
Bank-Management-System/
│
├── bank_management.py
├── bank_data.json
└── README.md
bank_data.json is automatically created by the application when account data is saved.
Requirements
Make sure Python 3 is installed on your computer.

Check your Python version:

python --version
or:

python3 --version
No external Python libraries are required.

Installation
1. Clone the repository
git clone <your-repository-url>
2. Navigate to the project directory
cd Bank-Management-System
3. Run the application
python bank_management.py
Application Menu
When the application starts, the following menu is displayed:

========== BANK MANAGEMENT SYSTEM ==========
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Account Details
6. Exit
============================================
1. Create Account
Users can create a new bank account by providing:

Account number
Account holder name
Phone number
Initial deposit
2. Deposit Money
Users can enter their account number and deposit money into their account.

3. Withdraw Money
Users can withdraw money from their account if sufficient balance is available.

4. Check Balance
Users can view the current balance of their bank account.

5. Account Details
Users can view:

Account number
Account holder name
Phone number
Current balance
6. Exit
Closes the Bank Management System.

Data Storage
The application uses a file named bank_data.json to store account information.

Example:

{
    "1001": {
        "name": "John",
        "phone": "9876543210",
        "balance": 5000
    }
}
This allows account information to remain available even after the application is closed.

Example
Enter your choice: 1

Enter account number: 1001
Enter account holder name: John
Enter phone number: 9876543210
Enter initial deposit: 5000

Account created successfully!
Deposit example:

Enter your choice: 2

Enter account number: 1001
Enter amount to deposit: 2000

₹2000.00 deposited successfully.
Current balance: ₹7000.00
Validation
The application checks for:

Duplicate account numbers
Invalid account numbers
Negative deposits
Invalid withdrawal amounts
Insufficient account balance
Invalid menu choices
Invalid numeric input
Limitations
This project is intended for educational purposes. It is a basic command-line application and should not be used for handling real banking transactions.

For a production-level banking application, additional features such as authentication, encryption, database security, transaction logging, and authorization would be required.

Future Enhancements
Possible improvements include:

User login and authentication
Admin login
MySQL/PostgreSQL database
Transaction history
Money transfer between accounts
Account deletion
Account update
Interest calculation
Password/PIN protection
Graphical User Interface (GUI)
Web-based interface
PDF transaction statements
License
This project is created for educational and learning purposes. :::

You can copy this directly into a file named README.md and upload it with your Python project.


