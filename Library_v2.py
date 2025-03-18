class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title= title
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        self.borrower = None
        book_list.append(self)

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("####################")


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.borrowed_books = []
        user_list.append(self)

def user_details(self):
    print("Name:", self.name)
    print("Address:", self.address)
    print("Fees $", self.fees)
    print("####################")

def print_users():
    for user in user_list:
        user.user_details()

def print_info():
    for book in book_list:
        book.book_details()

def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address, "has been added to the user list.")


book_list = []
user_list = []

Book("Lord of Ring", "J.R.R.Tolkien", "TOL", "97802611")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25 Appletree Dr")
User("Mary", "8 Moon Cres")

add_user()



