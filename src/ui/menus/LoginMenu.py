import os
from src.data.Users import Users
import MainMenu

class LoginMenu:

    #gets user data
    global strawhats
    strawhats = Users.getUsers()
    global onPassword = False
    global username
    global invalid = False

    #
    def loginMenu(error=False):
        print()
        print("=======Login Menu=======")
        print()
        if onPassword = False:
            if error = True:
                print("\033[3m" + "Invalid Username" + "\033[3m")
                if invalid: print("\033[3m" + "Please put an available option" + "\033[3m")
                print("[1] Try Again")
                print("[2] Return to Main Menu")
                input = input("")
            else:
                input = input("Please enter your USERNAME: ")
            if(input == "1"):
                invalid = False
                LoginMenu.loginMenu()
            if(input == "2"):
                invalid = False
                MainMenu.mainMenu()
            else:
                os.system("cls")
                invalid = True
                LoginMenu.loginMenu(True)
        else:
            pass
        if onPassword = True:
            print("Please enter your USERNAME: " + username)
        elif LoginMenu.checkUsername(input):
            username = input
            onPassword = True
        else:
            LoginMenu.reRunLoginMenu()
        input = input("Please enter your PASSWORD: ")
        if LoginMenu.checkPassword(input):
            #logged in
        else

        if error: print("\033[3m" + "Please put an available option" + "\033[3m")
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
        if username in strawhats:
            return True
        else:
            return False

    def checkPassword(password):
        if password == strawhats[username]["login"]:
            return True
        else:
            return False

    def reRunLoginMenu():
        os.system("cls")
        LoginMenu.loginMenu(True)

