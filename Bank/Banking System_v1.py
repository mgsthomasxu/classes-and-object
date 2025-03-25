# Question 1

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
    # TO COMPLETE

    True

def overdrafts():
    # TO COMPLETE

    True

def missingEmails():
    # TO COMPLETE

    True

def bankDetails():
    # TO COMPLETE

    True

def transfer():
    # TO COMPLETE

    True

user_list = []
GenerateUsers()

# test to print displayinfo
for user in user_list:
    user.displayInfo()

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

