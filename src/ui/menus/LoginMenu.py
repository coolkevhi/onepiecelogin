import os
from src.data.Users import Users

class LoginMenu:

    #gets user data
    Users = Users.getUsers()

    #
    def loginMenu(error=False):
        print()
        print("=======Login Menu=======")
        print()
        input = input("Please enter your USERNAME: ")
        if LoginMenu.checkUsername(input):
            return ""
        else:

        print("[2] Quit")
        if error: print("\033[3m" + "Please put an available option" + "\033[3m")
        choice = input("")
        if choice == "1":
            os.system("cls")
            print("WIP")
        elif choice == "2":
            print("Thanks for using the program!")
            SystemExit()
        else:
            os.system("cls")
            LoginMenu.loginMenu(True)

    #
    def checkUsername(username):
        if username in Users:
            return True
        else:
            return False
