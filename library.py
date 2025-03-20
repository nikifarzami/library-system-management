from string import ascii_letters as alphabet
from datetime import datetime

date = datetime.now().date()

def main_menu():
        while True:
                print("Main Menu:\n")
                print("1. Librarian:\n")
                print("2. Member:\n")
                print("3. Exit:\n")

                try:
                        choice = int(input("Enter your Choice Please: "))
                        if choice == 1:
                                librarian_menu()
                        elif choice == 2:
                                member_menu()
                        elif choice == 3:
                                print("Exiting")
                                break
                        else:
                                print("Invalid Choice. Choose Again!")
                except ValueError:
                        print("Error, enter a number. ")

def librarian_menu():
        while True:
                print("Librarian Menu: \n")
                print("1. Add a New Book\n ")
                print("2. Update Book details\n")
                print("3. Remove a Book\n")
                print("4. View All Books\n")
                print("5. Manage Members:\n")
                print("6. Exit\n")

                try:
                        choice = int(input("Enter your Choice: "))
                        if choice == 1:
                                add_book()
                        elif choice == 2:
                                update_book()
                        elif choice == 3:
                                remove_book()
                        elif choice == 4:
                                view_book()
                        elif choice == 5:
                                manage_member()
                        elif choice == 6:
                                break
                        else:
                                print("Invalid Choice. Choose Again!")
                except ValueError:
                        print("Error , enter a number. ")

def member_menu():
        while True:
                print(" Member Menu :\n")
                print("1. Search for a Book:\n")
                print("2. Borrow a Book:\n ")
                print("3. Return a Book: \n")
                print("4. View borrowed Books:\n ")
                print("5. Exit\n")

                try:
                        choice = int(input("Enter you Choice: "))
                        if choice == 1:
                                search_book()
                        elif choice == 2:
                                borrow_book()
                        elif choice == 3:
                                return_book()
                        elif choice == 4:
                                view_borrowed_book()
                        elif choice == 5:
                                break
                        else:
                                print("Invalid Choice. Choose Again!")
                except ValueError:
                        print("Error , enter a number. ")

def add_book():
        while True:
                book_name = input("Enter Book's Title:\n")
                if all(char in alphabet + " " for char in book_name):
                        break
                else:
                        print("Error, reEnter again. ")
        while True:
                author_name = input("please enter author: ")
                if all(char in alphabet + " " for char in author_name):
                        break
                else:
                        print("Error , reEnter. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
                        for book in books:
                                title, _ = book.strip().split(",")
                                if title.lower() == book_name.lower():
                                        print(f"{book_name}  exists!")
                                        return
        except FileNotFoundError:
                pass

        with open("books.txt", "a") as file:
                file.write(f"{book_name}, {author_name}\n")
        print(f"{book_name} by {author_name} added successfully!")

def update_book():
        while True:
                book_name = input("Enter Book's Title to update:\n")
                if all(char in alphabet + " " for char in book_name):
                        break
                else:
                        print("Error, reEnter again. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                print("No book was found.")
                return

        new_library = []
        found = False
        for book in books:
                title, author = book.strip().split(",")
                if title.lower() == book_name.lower():
                        found = True
                        while True:
                                new_author = input("Enter new author: ")
                                if all(char in alphabet + " " for char in new_author):
                                        break
                                else:
                                        print("Error , reEnter. ")
                        new_library.append(f"{title}, {new_author}\n")
                        print(f"Updated {title} with new author: {new_author}")
                else:
                        new_library.append(book)

        if not found:
                print(f"{book_name} isn't in the library.")
        else:
                with open("books.txt", "w") as file:
                        file.writelines(new_library)

def remove_book():
        while True:
                remove_book = input("Enter Book's title: \n")
                if all(char in alphabet + " " for char in remove_book):
                        break
                else:
                        print("Error , reEnter. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                print("No book was found.")
                return

        new_library = []
        found = False
        for book in books:
                try:
                        title, author = book.strip().split(",")
                        if title.lower() == remove_book.lower():
                                found = True
                                print(f"Book: {title}, Author: {author} has been deleted.")
                        else:
                                new_library.append(book)
                except ValueError:
                        print(f"bad entry: {book.strip()}")

        if not found:
                print(f"{remove_book} isn't in the library.")

        with open("books.txt", "w") as file:
                file.writelines(new_library)

def view_book():
        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                print("Library is empty")
                return

        if not books:
                print("library is  empty ")
                return

        print("Books list: ")
        for book in books:
                try:
                        title, author = book.strip().split(",")
                        print(f"Book: {title}, Author: {author}")
                except ValueError:
                        print(f"bad entry: {book.strip()}")

def search_book():
        while True:
                search = input("Enter Book's title to search:\n")
                if all(char in alphabet + " " for char in search):
                        break
                else:
                        print("Error, reEnter again. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                print("No book was found.")
                return

        found = False
        for book in books:
                try:
                        title, author = book.strip().split(",")
                        if search.lower() in title.lower():
                                print(f"Found - Book: {title}, Author: {author}")
                                found = True
                except ValueError:
                        print(f"Skipping bad entry: {book.strip()}")

        if not found:
                print(f"{search} isn't in the library.")

def borrow_book():
        while True:
                member_name = input("Enter your name: ")
                if all(char in alphabet + " " for char in member_name):
                        break
                else:
                        print("Error , reEnter. ")
        while True:
                book_name = input("Enter Book's Title to borrow:\n")
                if all(char in alphabet + " " for char in book_name):
                        break
                else:
                        print("Error, reEnter again. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                print("No book was found.")
                return

        found = False
        for book in books:
                title, author = book.strip().split(",")
                if title.lower() == book_name.lower():
                        found = True
                        with open("borrowed.txt", "a") as file:
                                file.write(f"{member_name}, {title}, {author}, {date}\n")
                        print(f"{title} borrowed by {member_name}!")
                        break

        if not found:
                print(f"{book_name} isn't in the library.")

def return_book():
        while True:
                member_name = input("Enter your name: ")
                if all(char in alphabet + " " for char in member_name):
                        break
                else:
                        print("Error , reEnter. ")
        while True:
                book_name = input("Enter Book's Title to return:\n")
                if all(char in alphabet + " " for char in book_name):
                        break
                else:
                        print("Error, reEnter again. ")

        try:
                with open("borrowed.txt", "r") as file:
                        borrowed = file.readlines()
        except FileNotFoundError:
                print("No borrowed books found.")
                return

        new_borrowed = []
        found = False
        for entry in borrowed:
                try:
                        name, title, author, borrow_date = entry.strip().split(", ")
                        if name.lower() == member_name.lower() and title.lower() == book_name.lower():
                                found = True
                                print(f"{title} returned by {member_name}!")
                        else:
                                new_borrowed.append(entry)
                except ValueError:
                        print(f"Skipping bad entry: {entry.strip()}")

        if not found:
                print(f"No record of {member_name} borrowing {book_name}.")
        else:
                with open("borrowed.txt", "w") as file:
                        file.writelines(new_borrowed)

def view_borrowed_book():
        while True:
                member_name = input("Enter your name: ")
                if all(char in alphabet + " " for char in member_name):
                        break
                else:
                        print("Error , reEnter. ")

        try:
                with open("borrowed.txt", "r") as file:
                        borrowed = file.readlines()
        except FileNotFoundError:
                print("No borrowed books found.")
                return

        found = False
        print(f"Borrowed books by {member_name}: ")
        for entry in borrowed:
                try:
                        name, title, author, borrow_date = entry.strip().split(", ")
                        if name.lower() == member_name.lower():
                                print(f"Book: {title}, Author: {author}, Borrowed on: {borrow_date}")
                                found = True
                except ValueError:
                        print(f"bad entry: {entry.strip()}")

        if not found:
                print(f"No books borrowed by {member_name}.")

def manage_member():
        while True:
                print("1. Add member:\n")
                print("2. View all members:\n")
                print("3. Remove  member:\n")
                print("4. Search member:\n")
                print("5. Exit:\n")

                try:
                        choice = int(input("Enter your Choice Please: "))
                        if choice == 1:
                                print("Add Member Section\n")
                                while True:
                                        member_name = input("Enter member's name: ")
                                        if all(char in alphabet + " " for char in member_name):
                                                break
                                        else:
                                                print("Error, reEnter. ")
                                with open("member.txt", "a") as file:
                                        file.write(f"{member_name}, added on {date}\n")
                                print(f"{member_name} added successfully!")

                        elif choice == 2:
                                print(" View All Member:\n")
                                try:
                                        with open("member.txt", "r") as file:
                                                members = file.readlines()
                                except FileNotFoundError:
                                        print("library is  empty ")
                                        return
                                if not members:
                                        print("library is  empty ")
                                else:
                                        print("member list: ")
                                        for member in members:
                                                print(member.strip())

                        elif choice == 3:
                                while True:
                                        remove_member = input("Enter  choice member's : \n")
                                        if all(char in alphabet + " " for char in remove_member):
                                                break
                                        else:
                                                print("Error , reEnter. ")
                                try:
                                        with open("member.txt", "r") as file:
                                                members = file.readlines()
                                except FileNotFoundError:
                                        print("No member was found.")
                                        return

                                updated_members = []
                                found = False
                                for member in members:
                                        try:
                                                name, _ = member.strip().split(", added on ")
                                                if name.lower() == remove_member.lower():
                                                        found = True
                                                        print(f"member {name} has been removed.")
                                                else:
                                                        updated_members.append(member)
                                        except ValueError:
                                                print(f"Skipping bad entry: {member.strip()}")

                                if not found:
                                        print(f"member {remove_member} not found.")
                                else:
                                        with open("member.txt", "w") as file:
                                                file.writelines(updated_members)

                        elif choice == 4:
                                print("Search member section:\n")
                                while True:
                                        search = input("enter the name of the member: ")
                                        if all(char in alphabet + " " for char in search):
                                                break
                                        else:
                                                print("Error , reEnter. ")
                                try:
                                        with open("member.txt", "r") as file:
                                                members = file.readlines()
                                except FileNotFoundError:
                                        print("No member found!!!")
                                        return

                                found = False
                                for member in members:
                                        try:
                                                name, _ = member.strip().split(", added on ")
                                                if search.lower() in name.lower():
                                                        print(f"member found: {member.strip()}")
                                                        found = True
                                        except ValueError:
                                                print(f"bad entry: {member.strip()}")

                                if not found:
                                        print(f"no member found with {search}.")

                        elif choice == 5:
                                break
                        else:
                                print("Invalid Choice. Choose Again!")
                except ValueError:
                        print("Error , enter a number. ")

main_menu()
