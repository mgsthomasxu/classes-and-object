# Question 6

class User:
    def __init__(self, first_name, last_name, gender, street_address, city,email, cc_number, cc_type, balance, account_no):
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
        user_list.append(self)

    def displayInfo(self):
        print("##################################")
        print(f"First Name   : {self.first_name}")
        print(f"Last Name    : {self.last_name}")
        print(f"Gender       : {self.gender}")
        print(f"Street       : {self.street_address}")
        print(f"City         : {self.city}")
        print(f"Email        : {self.email}")
        print(f"CC Number    : {self.cc_number}")
        print(f"CC Type      : {self.cc_type}")
        print(f"Balance      : {self.balance}")
        print(f"Account No   : {self.account_no}")
        print("##################################\n")


def GenerateUsers():
    import csv
    with open('bankUsers.csv', newline='', encoding='utf-8-sig') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    name_input = input("Enter the full name of the user \n"
                       "(Space between first name, last name): ")
    user_found = False
    for user in user_list:
        full_name = f"{user.first_name} {user.last_name}"
        if full_name.lower() == name_input.lower():
            user.displayInfo()
            user_found = True
            break
    if user_found:
        print("User found successfully.")
    else:
        print("User not found. Try again.")

def overdrafts():
    print("Users that overdraft：")
    count_overdrafts = 0
    total_overdraft = 0.0
    for user in user_list:
        if user.balance < 0:
            print(f"{user.first_name} {user.last_name}")
            count_overdrafts += 1
            total_overdraft += user.balance
    print(f"\nTotal number of users with overdrafts: {count_overdrafts}"
          f"Total amount overdraft by these users: ${total_overdraft}")


def missingEmails():
    no_email_users = 0
    for user in user_list:
        if not user.email:
            print(f"{user.first_name} {user.last_name}")
            no_email_users += 1
    print(f"\nThe total number of users with no email: {no_email_users}")


def bankDetails():
    total_users = 0
    total_worth = 0
    for user in user_list:
        total_users += 1
        total_worth += user.balance
    print(f"Total users: {total_users}"
          f"Total worth: {total_worth}")


def transfer():
    # Search for user
    withdraw_account = input("Enter the account number to transfer from : ")
    withdraw_user = None
    for user in user_list:
        if str(user.account_no) == withdraw_account:
            withdraw_user = user
            print(f"\nUser is: {withdraw_user.first_name} "
                  f"{withdraw_user.last_name}\n"
                  f"Account No: {withdraw_user.account_no}\nBalance ${withdraw_user.balance}")
            break

    if not withdraw_user:
        print("no account number found.")
        return

    # Get the transfer amount
    transfer_amount = input("\nHow much do you want to transfer? $")
    try:
        transfer_amount = float(transfer_amount)
    except ValueError:
        print("Please enter the amount of money.")
        return
    deposit_account = input("\nEnter the account number you want to transfer money to: ")
    deposit_user = None
    for user in user_list:
        if str(user.account_no) == deposit_account:
            deposit_user = user
            break
    if not deposit_user:
        print("account number not found.")
        return

    # Confirm transfer
    confirm = input(f"\nDo you want to transfer ${transfer_amount} to {deposit_user.first_name} "
                    f"{deposit_user.last_name}? (Press enter to confirm or any other key to cancel): ")

    if confirm == "":
        withdraw_user.balance -= transfer_amount
        deposit_user.balance += transfer_amount

        print(f"${transfer_amount} has been transfer\n"
              f"from {withdraw_user.first_name} {withdraw_user.last_name} "
              f"the original balance of ${withdraw_user.balance}\n"
              f"to {deposit_user.first_name} {deposit_user.last_name} "
              f"the new balance of ${deposit_user.balance}")
    else:
        print("Transfer cancelled.")

user_list = []
GenerateUsers()


userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()

