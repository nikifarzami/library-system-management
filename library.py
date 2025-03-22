from string import ascii_letters as alphabet
from datetime import datetime
from flask import Flask, request, render_template
import sys

app = Flask(__name__)

date = datetime.now().date()

def main_menu():
        if 'request' in globals() and request.method == 'GET':  
                return render_template('main_menu.html')
        else:  
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

@app.route('/')
def main_menu_web():
        return main_menu()

@app.route('/librarian')
def librarian_menu():
        if 'request' in globals() and request.method == 'GET':  
                return render_template('librarian_menu.html')
        else:  
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

@app.route('/member')
def member_menu():
        if 'request' in globals() and request.method == 'GET':  
                return render_template('member_menu.html')
        else:  
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

@app.route('/add_book', methods=['POST'])
def add_book():
        if 'request' in globals() and request.method == 'POST':  # Flask mode
                book_name = request.form['book_name']
                author_name = request.form['author_name']
        else:  # Console mode
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

        if not all(char in alphabet + " " for char in book_name):
                if 'request' in globals():
                        return render_template('message.html', message="Error, reEnter again. ")
                else:
                        print("Error, reEnter again. ")
                        return
        if not all(char in alphabet + " " for char in author_name):
                if 'request' in globals():
                        return render_template('message.html', message="Error , reEnter. ")
                else:
                        print("Error , reEnter. ")
                        return

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
                        for book in books:
                                title, _ = book.strip().split(",")
                                if title.lower() == book_name.lower():
                                        if 'request' in globals():
                                                return render_template('message.html', message=f"{book_name} already exists!")
                                        else:
                                                print(f"{book_name} already exists!")
                                                return
        except FileNotFoundError:
                pass

        with open("books.txt", "a") as file:
                file.write(f"{book_name}, {author_name}\n")
        if 'request' in globals():
                return render_template('message.html', message=f"{book_name} by {author_name} added successfully!", back_link="/librarian")
        else:
                print(f"{book_name} by {author_name} added successfully!")

@app.route('/update_book', methods=['POST'])
def update_book():
        if 'request' in globals() and request.method == 'POST':  
                book_name = request.form['book_name']
                new_author = request.form['new_author']
        else:  
                while True:
                        book_name = input("Enter Book's Title to update:\n")
                        if all(char in alphabet + " " for char in book_name):
                                break
                        else:
                                print("Error, reEnter again. ")
                while True:
                        new_author = input("Enter new author: ")
                        if all(char in alphabet + " " for char in new_author):
                                break
                        else:
                                print("Error , reEnter. ")

        if not all(char in alphabet + " " for char in book_name):
                return "Error, reEnter again. " if 'request' in globals() else print("Error, reEnter again. ")
        if not all(char in alphabet + " " for char in new_author):
                return "Error , reEnter. " if 'request' in globals() else print("Error , reEnter. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                return "No book was found." if 'request' in globals() else print("No book was found.")

        new_library = []
        found = False
        for book in books:
                title, author = book.strip().split(",")
                if title.lower() == book_name.lower():
                        found = True
                        new_library.append(f"{title}, {new_author}\n")
                        if 'request' in globals():
                                return f"Updated {title} with new author: {new_author}"
                        else:
                                print(f"Updated {title} with new author: {new_author}")
                else:
                        new_library.append(book)

        if not found:
                return f"{book_name} isn't in the library." if 'request' in globals() else print(f"{book_name} isn't in the library.")
        with open("books.txt", "w") as file:
                file.writelines(new_library)

@app.route('/remove_book', methods=['POST'])
def remove_book():
        if 'request' in globals() and request.method == 'POST':  
                remove_book = request.form['remove_book']
        else:  
                while True:
                        remove_book = input("Enter Book's title: \n")
                        if all(char in alphabet + " " for char in remove_book):
                                break
                        else:
                                print("Error , reEnter. ")

        if not all(char in alphabet + " " for char in remove_book):
                return "Error , reEnter. " if 'request' in globals() else print("Error , reEnter. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                return "No book was found." if 'request' in globals() else print("No book was found.")

        new_library = []
        found = False
        for book in books:
                try:
                        title, author = book.strip().split(",")
                        if title.lower() == remove_book.lower():
                                found = True
                                if 'request' in globals():
                                        return f"Book: {title}, Author: {author} has been deleted."
                                else:
                                        print(f"Book: {title}, Author: {author} has been deleted.")
                        else:
                                new_library.append(book)
                except ValueError:
                        return f"Skipping bad entry: {book.strip()}" if 'request' in globals() else print(f"Skipping bad entry: {book.strip()}")

        if not found:
                return f"{remove_book} isn't in the library." if 'request' in globals() else print(f"{remove_book} isn't in the library.")
        with open("books.txt", "w") as file:
                file.writelines(new_library)

@app.route('/view_book')
def view_book():
        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                if 'request' in globals():
                        return render_template('message.html', message="Library is empty")
                else:
                        print("Library is empty")
                        return
        
        if not books:
                if 'request' in globals():
                        return render_template('message.html', message="library is  empty ")
                else:
                        print("library is  empty ")
                        return
        
        book_list = []
        for book in books:
                try:
                        title, author = book.strip().split(",")
                        book_list.append({"title": title, "author": author})
                except ValueError:
                        if 'request' in globals():
                                book_list.append({"title": f"Skipping bad entry: {book.strip()}", "author": ""})
                        else:
                                print(f"Skipping bad entry: {book.strip()}")

        if 'request' in globals():
                return render_template('view_book.html', books=book_list)
        else:
                print("Books list: ")
                for book in book_list:
                        print(f"Book: {book['title']}, Author: {book['author']}")

@app.route('/search_book', methods=['POST'])
def search_book():
        if 'request' in globals() and request.method == 'POST':  
                search = request.form['search']
        else:  
                while True:
                        search = input("Enter Book's title to search:\n")
                        if all(char in alphabet + " " for char in search):
                                break
                        else:
                                print("Error, reEnter again. ")

        if not all(char in alphabet + " " for char in search):
                return "Error, reEnter again. " if 'request' in globals() else print("Error, reEnter again. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                return "No book was found." if 'request' in globals() else print("No book was found.")

        found = False
        if 'request' in globals():
                result = ""
                for book in books:
                        try:
                                title, author = book.strip().split(",")
                                if search.lower() in title.lower():
                                        result += f"Found - Book: {title}, Author: {author}<br>"
                                        found = True
                        except ValueError:
                                result += f"Skipping bad entry: {book.strip()}<br>"
                if not found:
                        return f"{search} isn't in the library."
                return result
        else:
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

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
        if 'request' in globals() and request.method == 'POST':  
                member_name = request.form['member_name']
                book_name = request.form['book_name']
        else:  
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

        if not all(char in alphabet + " " for char in member_name):
                return "Error , reEnter. " if 'request' in globals() else print("Error , reEnter. ")
        if not all(char in alphabet + " " for char in book_name):
                return "Error, reEnter again. " if 'request' in globals() else print("Error, reEnter again. ")

        try:
                with open("books.txt", "r") as file:
                        books = file.readlines()
        except FileNotFoundError:
                return "No book was found." if 'request' in globals() else print("No book was found.")

        found = False
        for book in books:
                title, author = book.strip().split(",")
                if title.lower() == book_name.lower():
                        found = True
                        with open("borrowed.txt", "a") as file:
                                file.write(f"{member_name}, {title}, {author}, {date}\n")
                        if 'request' in globals():
                                return f"{title} borrowed by {member_name}!"
                        else:
                                print(f"{title} borrowed by {member_name}!")
                        break
        
        if not found:
                return f"{book_name} isn't in the library." if 'request' in globals() else print(f"{book_name} isn't in the library.")

@app.route('/return_book', methods=['POST'])
def return_book():
        if 'request' in globals() and request.method == 'POST':  
                member_name = request.form['member_name']
                book_name = request.form['book_name']
        else:  
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

        if not all(char in alphabet + " " for char in member_name):
                return "Error , reEnter. " if 'request' in globals() else print("Error , reEnter. ")
        if not all(char in alphabet + " " for char in book_name):
                return "Error, reEnter again. " if 'request' in globals() else print("Error, reEnter again. ")

        try:
                with open("borrowed.txt", "r") as file:
                        borrowed = file.readlines()
        except FileNotFoundError:
                return "No borrowed books found." if 'request' in globals() else print("No borrowed books found.")

        new_borrowed = []
        found = False
        for entry in borrowed:
                try:
                        name, title, author, borrow_date = entry.strip().split(", ")
                        if name.lower() == member_name.lower() and title.lower() == book_name.lower():
                                found = True
                                if 'request' in globals():
                                        return f"{title} returned by {member_name}!"
                                else:
                                        print(f"{title} returned by {member_name}!")
                        else:
                                new_borrowed.append(entry)
                except ValueError:
                        return f"Skipping bad entry: {entry.strip()}" if 'request' in globals() else print(f"Skipping bad entry: {entry.strip()}")

        if not found:
                return f"No record of {member_name} borrowing {book_name}." if 'request' in globals() else print(f"No record of {member_name} borrowing {book_name}.")
        with open("borrowed.txt", "w") as file:
                file.writelines(new_borrowed)

@app.route('/view_borrowed_book', methods=['POST'])
def view_borrowed_book():
        if 'request' in globals() and request.method == 'POST':  
                member_name = request.form['member_name']
        else:  
                while True:
                        member_name = input("Enter your name: ")
                        if all(char in alphabet + " " for char in member_name):
                                break
                        else:
                                print("Error , reEnter. ")

        if not all(char in alphabet + " " for char in member_name):
                return "Error , reEnter. " if 'request' in globals() else print("Error , reEnter. ")

        try:
                with open("borrowed.txt", "r") as file:
                        borrowed = file.readlines()
        except FileNotFoundError:
                return "No borrowed books found." if 'request' in globals() else print("No borrowed books found.")

        found = False
        if 'request' in globals():
                result = f"Borrowed books by {member_name}: <br>"
                for entry in borrowed:
                        try:
                                name, title, author, borrow_date = entry.strip().split(", ")
                                if name.lower() == member_name.lower():
                                        result += f"Book: {title}, Author: {author}, Borrowed on: {borrow_date}<br>"
                                        found = True
                        except ValueError:
                                result += f"Skipping bad entry: {entry.strip()}<br>"
                if not found:
                        return f"No books borrowed by {member_name}."
                return result
        else:
                print(f"Borrowed books by {member_name}: ")
                for entry in borrowed:
                        try:
                                name, title, author, borrow_date = entry.strip().split(", ")
                                if name.lower() == member_name.lower():
                                        print(f"Book: {title}, Author: {author}, Borrowed on: {borrow_date}")
                                        found = True
                        except ValueError:
                                print(f"Skipping bad entry: {entry.strip()}")
                if not found:
                        print(f"No books borrowed by {member_name}.")

@app.route('/manage_member', methods=['GET', 'POST'])
def manage_member():
        if 'request' in globals() and request.method == 'GET':  
                return render_template('manage_member.html')
        elif 'request' in globals() and request.method == 'POST':  
                choice = request.form['choice']
        else:  
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
                                                        print(f"Skipping bad entry: {member.strip()}")
                                        if not found:
                                                print(f"no member found with {search}.")
                                elif choice == 5:
                                        break
                                else:
                                        print("Invalid Choice. Choose Again!")
                        except ValueError:
                                print("Error , enter a number. ")

        if choice == '1':
                member_name = request.form['member_name']
                if not all(char in alphabet + " " for char in member_name):
                        return "Error, reEnter. "
                with open("member.txt", "a") as file:
                        file.write(f"{member_name}, added on {date}\n")
                return f"{member_name} added successfully!"
        
        elif choice == '2':
                try:
                        with open("member.txt", "r") as file:
                                members = file.readlines()
                except FileNotFoundError:
                        return "library is  empty "
                if not members:
                        return "library is  empty "
                result = "member list: <br>"
                for member in members:
                        result += f"{member.strip()}<br>"
                return result
        
        elif choice == '3':
                remove_member = request.form['remove_member']
                if not all(char in alphabet + " " for char in remove_member):
                        return "Error , reEnter. "
                try:
                        with open("member.txt", "r") as file:
                                members = file.readlines()
                except FileNotFoundError:
                        return "No member was found."

                updated_members = []
                found = False
                for member in members:
                        try:
                                name, _ = member.strip().split(", added on ")
                                if name.lower() == remove_member.lower():
                                        found = True
                                        return f"member {name} has been removed."
                                else:
                                        updated_members.append(member)
                        except ValueError:
                                return f"Skipping bad entry: {member.strip()}"

                if not found:
                        return f"member {remove_member} not found."
                with open("member.txt", "w") as file:
                        file.writelines(updated_members)
        
        elif choice == '4':
                search = request.form['search']
                if not all(char in alphabet + " " for char in search):
                        return "Error , reEnter. "
                try:
                        with open("member.txt", "r") as file:
                                members = file.readlines()
                except FileNotFoundError:
                        return "No member found!!!"

                found = False
                result = ""
                for member in members:
                        try:
                                name, _ = member.strip().split(", added on ")
                                if search.lower() in name.lower():
                                        result += f"member found: {member.strip()}<br>"
                                        found = True
                        except ValueError:
                                result += f"Skipping bad entry: {member.strip()}<br>"

                if not found:
                        return f"no member found with {search}."
                return result

if __name__ == "__main__":
        if len(sys.argv) > 1 and sys.argv[1] == "console":
                main_menu()
        else:
                app.run(debug=True)
