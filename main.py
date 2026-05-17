######## Lets name this app as LibServ:- Libarary Management Service
#Main file, which would be front face to the user
import sys
from AuthenticationService import AuthenticationService
from LibManagementService import LibManagementService


#Keep on continous loop and show multiple options with keys, ask user to type Exit to close this app

class LibServApp:

    def __init__(self):
        self.authService = AuthenticationService()
        self.libManagSrvc = LibManagementService()
        self.max_invalidCount = 3
        self.failed_login = 0

    def load(self):
        print("------  * WELCOME TO THE LibSerV * ------- ")
        print("*********************************************\n")

        while self.failed_login < self.max_invalidCount:
            user_id = input(f"\nEnter user id: ")
            user_password = input("Enter password: ")

            if self.authService.is_valid_user(user_id, user_password):
                print(f"\nWelcome, {user_password}! You are Logged in successful.")
                ##add main logic
                self.libservOptions()
                return
            else:
                self.failed_login += 1
                if self.failed_login < self.max_invalidCount:
                    print(f"\nPlease entry the correct credentials.")


        print("Too many failed attempts. Access Locked. Exiting application...")
        sys.exit()

    def libservOptions(self):
        '''Show all the available menus to user'''
        while True:
            print("\n--- LibSerV OPTIONS ---")
            print("1. Borrow a Book")
            print("2. Return a Book")
            print("3. Show Available Books")
            print("4. Exit Application")

            selectedOption = input("\nPlease select an option (1-4): ")

            if selectedOption == "1":
                ## borrow book function call
                memberId = input("Enter Member ID: ")
                bookId = input("Enter Book ID: ")
                result = self.libManagSrvc.borrow_book(memberId, bookId)
                print(f"\n{result}")

            elif selectedOption == "2":
                ## Return book function call
                memberId = input("Enter Member ID: ")
                bookId = input("Enter Book ID: ")
                result = self.libManagSrvc.return_book(memberId, bookId)
                print(f"\n{result}")

            elif selectedOption == "3":
                ## show all available books to user
                results = self.libManagSrvc.show_available_books()
                if results:
                    for book in results: print(book)
                else:
                    print("Sorry No available books currently!")
                
            elif selectedOption == "4":
                ##Exit
                print("Thank you for using the LibSerV!")
                break
            else:
                print("Please help to select valid option")


if __name__ == "__main__":
    app = LibServApp()
    app.load()



