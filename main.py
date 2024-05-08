from book import Books
from user import User
from author import Author

harry_potter1 = Books("Harry 1", "JKR","01234" ,"Fiction", "2021")
harry_potter2 = Books("Harry 2", "JKR","01234" ,"Fiction","2022")

harsh = User("Harsh", "Denver, CO", "9998889999")
neha = User("Neha", "Superior, CO", "9998889998")

jkr = Author("JKR", "Bio Blah blah")

def main():
    books = [harry_potter1, harry_potter2]
    users = [harsh, neha]
    authors = [jkr]
    current_user = None
    while True:
        choice = input('''
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit       
        Please enter your choice: ''')
        if choice == "1":
            books = book_ops(books, current_user, authors)
        elif choice == "2":
            # current_user = user_actions(users)
            us1 = user_actions(users)
            users = us1[0]
            current_user = us1[1]
            # print(users)
            # print(current_user.name)
            print("\nCurrent User is", current_user.name if current_user != None else "None")
        elif choice == "3":
            author_ops(authors)
        elif choice == "4":
            break
        else:
            print("\nPlease enter a numeric value between 1 and 4 and try again!!!")

def book_ops(books, current_user, authors):
    # print(books)
    while True:
        choice = input('''
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books   
        6. Main Menu              
        Please enter your choice: ''')
        
        if choice == "1":
            return_f = add_book(authors)
            authors = return_f[0]
            new_book = return_f[1]
            books.append(new_book)
            return books
        elif choice == "2":
            if current_user != None:
                for idx, book in enumerate(books):

                    if book.is_available:
                        print(f"{idx+1}. {book.get_info()} ")
                book_num = int(input("Please enter book number to borrow: "))
                book_num2 = book_num - 1
                # current_user.borrow(book[book_num2])
                for idx, book in enumerate(books):
                    if idx == book_num2:
                        current_user.borrow(book)
                return books
            else:
                print("Please select a Current User before trying to borrow!!!")
                return books
                break
        elif choice == "3":
            if current_user != None:
                if current_user.book:
                    current_user.return_book()
                    return None
                else:
                    print("You have no books to return")
                    # return current_user
                    return books
            else:
                print("Please select a Current User before trying to borrow!!!")
                return books
                break
        elif choice == "4":
            book_search = input("Please enter book name to search:")
            for book in books:
                if book_search == book:
                    print("Book Found")
                    book.get_info()
                    return books
                else:
                    print("Book not found")
                    return books
        elif choice == "5":
            for idx, book in enumerate(books):
                if book.is_available:
                    print(f"{idx+1}. {book.get_info()} ")
            return books
        elif choice == "6":
            return books
            break
        else:
            print("\nPlease enter a numeric value between 1 and 6 and try again!!!")
        

        
def add_book(authors):
    btitle = input("Title: ").title()
    bauthor2 = add_author(authors)
    authors.append(bauthor2)
    bauthor = bauthor2.name
    bisbn = input("ISBN: ")
    bgenre = input("Genre: ")
    bdate= input("Publication Date: ")
    new_book = Books(btitle, bauthor, bisbn, bgenre, bdate)
    print("Book Added")
    # print("\nNew Book Details:-")
    # new_book.get_info()
    return authors, new_book



def user_actions(users):
    while True:
        choice = input('''
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Select a Current User 
        5. Main Menu                     
        Please enter your choice: ''')
        if choice == "1":
            new_user = add_user()
            users.append(new_user)
            return users, new_user
        elif choice == "2":
            current_user = user_details(users)
            return users, current_user
        elif choice == "3":
            for idx, name in enumerate(users):
                print(f"{idx+1}. {name.name}")
                # pass
            return users, None
        elif choice == "4":
            for idx, name in enumerate(users):
                print(f"{idx+1}. {name.name}")
            user_choice = int(input("Please enter the user number you want to make the current user: ")) - 1
            current_user = users[user_choice]
            return users, current_user
            break
        elif choice == "5":
            return users, None
            break
        else:
            print("\nPlease enter a numeric value between 1 and 5 and try again!!!")



def add_user():
    name = input('Name: ').title()
    address = input('Address: ').title()
    phone = input('Phone: ')
    new_user = User(name, address, phone)
    # users.append(new_user)
    print('\nUser Created')
    print("New User Details:-")
    new_user.get_info()
    return new_user

def user_details(users):

    while True:
        name = input('Search Name: ').title()
        for user in users:
            if user.name == name:
                print('User Found!')
                user.get_info()
                return user
        
        action = input('No Response... try another name? y or n: ')
        if action == 'n':
            add_user()
        elif action == 'y':
            continue

def author_ops(authors):
    while True:
        choice = input('''
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors   
        4. Main Menu                    
        Please enter your choice: ''')
        if choice == "1":
            add_author(authors)
        elif choice == "2":
            for idx, auth in enumerate(authors):
                print(f"{idx+1}. {auth.name}")

            choice = input("Please input your choice: ")
            ac_choice = int(choice) - 1
            print("Author Name:", authors[ac_choice].name)
            print("Biography: ", authors[ac_choice].biography)
        elif choice == "3":
            for idx, auth in enumerate(authors):
                print(f"\n{idx+1}. {auth.name}, Biography: {auth.biography}")
        elif choice == "4":
            break
        else:
            print("\nPlease enter a numeric value between 1 and 4 and try again!!!")

def add_author(authors):
    name = input("Author Name: ")
    i = 0
    print(authors)
    for idx, auth in enumerate(authors):
        print (auth.name)
        if name == auth.name:
            i = 0
            # print("Author Found")
            print(auth.name)
            print(auth.biography)
            return auth
        else:
            i = 1
    if i == 1:
        biography = input("Please enter Authors Biography if any: ")
        new_author = Author(name, biography)
        print("Author Added")
        return new_author

main()