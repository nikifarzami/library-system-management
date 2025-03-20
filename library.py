from string import ascii_letters as alphabet
from datetime import datetime

date = datetime.now().date()

def main_menu():
        while True:
                print("Main Menu:\n")
                print("1. Librarian:\n")
                print("2. Member:\n")
                print("3. Exit:\n")

                choice = int(input("Enter your Choice Please: "))

                if choice == 1:
                        librarian_menu()
                        choice = int(input("Enter your Choice: "))
                        if choice > 5:
                                print("Invalid Choice. Choose Again!")
                        
                elif choice==2:
                        member_menu()
                        choice=int(input("Enter your choice: " ))
                        if choice==5:
                                print("Invalid Choice. Choose Again!")

                elif choice == 3:
                        print("Exiting")
                        break

                else:
                        print("Invalid Choice. Choose Again!")

def librarian_menu():
        print("Librarian Menu: \n")
        print("1. Add a New Book\n ")
        print("2. Update Book details\n")
        print("3. Remove a Book\n")
        print("4. View All Books\n")
        print("5. Manage Members:\n")
        print("6. Exit\n")
        

        choice = input("Enter your Choice")

        if choice==1:
                add_book()
        elif choice == 2:
                update_book(())
        elif choice==3:
                remove_book()
        elif choice==4:
                view_book()
        elif choice==5:
                manage_member()
                
def member_menu():
        print(" Member Menu :\n")
        print("1. Search for a Book:\n")
        print("2. Borrow a Book:\n ")
        print("3. Return a Book: \n")
        print("4. View borrowed Books:\n ")        
        print("5. Exit\n")

        choice = input("Enter you Choice: ")
        
        if choice == 1:
                search_book()
        elif choice == 2:
                borrow_book()
        elif choice == 3:
                return_book()
        elif choice == 4:
                view_borrowed_book()        

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

        with open("books.txt", "a") as file:
                file.write(f"{book_name}, {author_name}\n")

        print(f"{book_name} by {author_name} added successfully!")

def remove_book():
        while True:
                remove_book =input("Enter Book's title: \n") 
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

        new_library = [ ]
        found = False
        for book in books:
                title, author = book.strip().split(",")

                if title.lower() == remove_book.lower():
                        found = True
                        print(f"Book: {title}, Author: {author} has been deleted.")
                else:
                        new_library.append(book)
        
        if not found:
                print(f"{remove_book} isn't in the library.")

        with open("books.txt", "w") as file:
                file.writelines(new_library)

def manage_member():
        while True:
                print("1. Add member:\n")
                print("2. View all members:\n")
                print("3. Remove  member:\n")
                print("4. Search member:\n")

                choice =  int(input("Enter your Choice Please: "))

                if choice == 1:
                        print("Add Member Section\n")
                        
                        while True:

                                member_name = input("Enter member's name: ")

                                if all (char in alphabet + " " for char in member_name):
                                        break
                                else:
                                        print("Error, reEnter.")
                                

                                with open("member.txt", "a") as file:
                                        file.write(f"{member_name} is added on {date}")


                        
                        
                elif choice==2:
                        print(" View All Member:\n")
                        try:
                                with open("member.text","r") as file:
                                        members = file.readlines()
                        except FileNotFoundError:
                                print("library is  empty ")
                                return
                        if not members:
                                print("library is  empty ")
                                return
                        print("member list: ")
                        for member in members:      
                                print(member)
                        
                elif choice==3:
                        while True:
                                remove_member =input("Enter  choice member's : \n") 
                                if all(char in alphabet + " " for char in remove_member):
                                        break 
                                else:
                                        print("Error , reEnter. ")

                                try:
                                        with open("members.txt", "r") as file:
                                                members = file.readlines()
                                except FileNotFoundError:
                                        print("No member was found.")
                                        return

                                updated_members = []
                                found = False
                                
                                for member in members:
                                        name, _ = member.strip().split(", added on")
                                        if name.lower() == remove_member.lower():
                                                found = True
                                                print(f"member {name} has been removed.")
                                        else:
                                                updated_members.append(member)

                                if not found:
                                        print(f"member {remove_member} not found.")

                                with open("member.txt", "w") as file:
                                        file.writelines(updated_members)
                                        
                elif choice==4:
                        print("Search member section:\n")

                        search = input("enter the name of the member: ")

                        try:
                                with open("member.txt" , "r") as file:
                                        members = file.readlines()
                        except FileNotFoundError:
                                print("No member found!!!")
                                return
                        
                        found = False

                        for member in members:
                                name, _ = members.strip().split(", added on ")
                                if search.lower() in name.lower():
                                        print(f"member found: {member.strip()}")
                                        found = True

                        if not found:
                                print(f"no member found.")

                        elif choice == 5:
                                print("back to librarian menu: ")
                                break
                        else:
                                print("invalid choice. choose again.")

def view_book():
        try:
                with open("books.txt","r") as file:
                        books = file.readlines()

        except FileNotFoundError:
                print("Library is empty")
                return
        
        if not books:
                print("library is  empty ")
                return
        
        print("Books list: ")
        for book in books:      
                title, author = book.strip().split(",")
                print(f"Book: {title}, Author: {author}")
