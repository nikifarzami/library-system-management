def librarian_menu():
        print("Librarian Menu: \n")
        print("1. Add a New Book\n ")
        print("2. Update Book details\n")
        print("3. Remove a Book\n")
        print("4. View All Books\n")
        print("5. Manage Members:\n")
        print("6. Exit\n")


def member_menu():
        print(" Member Menu :\n")
        print("1. Search for a Book:\n")
        print("2. Borrow a Book:\n ")
        print("3. Return a Book: \n")
        print("4. View borrowed Books:\n ")        
        print("5. Exit\n")



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


main_menu()
