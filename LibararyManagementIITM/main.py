######## Lets name this app as LibServ:- Libarary Management Service
#Main file, which would be front face to the user
import sys
from AuthenticationService import AuthenticationService


#Keep on continous loop and show multiple options with keys, ask user to type Exit to close this app

class LibServApp:

    def __init__(self):
        self.authService = AuthenticationService()
        self.max_invalidCount = 3
        self.failed_login = 0

    def load(self):
        print("------  * WELCOME TO THE LibSerV * ------- ")
        print("*********************************************\n")

        while self.failed_login < self.max_invalidCount:
            user_id = input("Enter user id: ")
            user_password = input("Enter password: ")

            if self.authService.is_valid_user(user_id, user_password):
                print(f"\nWelcome, {user_password}! You are Logged in successful.")
                ##add main logic
                return
            else:
                self.failed_login += 1

        print("Too many failed attempts. Access Locked. Exiting application...")
        sys.exit()


if __name__ == "__main__":
    app = LibServApp()
    app.load()



