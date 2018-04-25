# Import Statements
class Authenticated:
    def __init__(self, username, password):
        user_auth = False
        pass_auth = False
        loginFile = open("names.cred" "r")
        # Loops until both username and password are correctly typed
        while user_auth == False or pass_auth == False:
            # Checkes if there are any accounts created
            if loginFile.readlines() != "":
                for names in loginFile.readlines():
                    if(names.startswith("Username:")):
                        # Cuts the string to remove the "Username:"
                        uname = names[-9:]
                        if username == uname:
                            user_auth = True
                        else:
                            print("username doesn't exist.  Please type \"/signup\" to create an account")
                    if(names.startswith("Password:")):
                        pswrd = names[-9:]
                        if(password == pswrd):
                            pass_auth = True
                        else:
                            print("Password doesn't match the one on file for", uname)
            else:
                # if there are no accounts then prompt to create one
                print ("There are currently no accounts made\nType \"/signup\" to create an account.")
                prompt = input("")
                if prompt == "/signup":
                    new_username = input("Please type a desired username: ")
                    new_password = input("Please type your password: ")
                    super_user = input("Please enter the Super User Password (hint: toor): ")
                    sign = SignUp()

                    SignUp().__init__(new_username, new_password, super_user)
        print("You have been authenticated!!!".upper())