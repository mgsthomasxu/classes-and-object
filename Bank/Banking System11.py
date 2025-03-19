import csv

class User:
    user_list = []

    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance,
                 account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        User.user_list.append(self)

    def display_info(self):
        print(f"Account No: {self.account_no}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.street_address}, {self.city}")
        print(f"Email: {self.email}")
        print(f"Credit Card Number: {self.cc_number}")
        print(f"Credit Card Type: {self.cc_type}")
        print(f"Balance: ${self.balance:.2f}")


def generate_users():
    try:
        with open('bankUsers.csv', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
            for line in filereader:
                if len(line) < 10:  # Ensure all required fields exist
                    print(f"Skipping incomplete record: {line}")
                    continue
                try:
                    balance = float(line[8])
                except ValueError:
                    balance = 0  # Default balance if missing or invalid

                User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], balance, line[9])
    except FileNotFoundError:
        print("Error: bankUsers.csv not found. Please ensure the file is in the correct location.")


def display_menu():
    print("Welcome")
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")


def find_user():
    account_no = input("Enter the account number to find: ")
    for user in User.user_list:
        if user.account_no == account_no:
            user.display_info()
            return
    print("User not found.")


def overdrafts():
    print("Users with overdraft:")
    overdraft_found = False
    for user in User.user_list:
        if user.balance < 0:
            user.display_info()
            overdraft_found = True
    if not overdraft_found:
        print("No users with overdrafts.")


def missing_emails():
    print("Users with missing emails:")
    missing_emails_found = False
    for user in User.user_list:
        if not user.email.strip():
            user.display_info()
            missing_emails_found = True
    if not missing_emails_found:
        print("No users with missing emails.")


def bank_details():
    print("Bank Details:")
    total_balance = sum(user.balance for user in User.user_list)
    print(f"Total number of accounts: {len(User.user_list)}")
    print(f"Total bank balance: ${total_balance:.2f}")


def transfer():
    sender_account = input("Enter sender's account number: ")
    receiver_account = input("Enter receiver's account number: ")
    try:
        amount = float(input("Enter transfer amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    sender = None
    receiver = None
    for user in User.user_list:
        if user.account_no == sender_account:
            sender = user
        elif user.account_no == receiver_account:
            receiver = user

    if sender and receiver:
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            print("Transfer successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Sender or receiver account not found.")


generate_users()

if not User.user_list:
    print("No users found. Please check the CSV file.")
else:
    user_choice = ""
    while user_choice != "Q":
        display_menu()
        user_choice = input("Enter choice: ").upper()
        print()
        if user_choice == "1":
            find_user()
        elif user_choice == "2":
            overdrafts()
        elif user_choice == "3":
            missing_emails()
        elif user_choice == "4":
            bank_details()
        elif user_choice == "5":
            transfer()
        print()
        
