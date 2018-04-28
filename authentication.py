# Import Statements
import signup
class Authenticated:
    def __init__(self, username, password):
        user_auth = False
        pass_auth = False
        loginFile = open("names.cred", "r")
        while user_auth == False or pass_auth == False:
            # Checkes if there are any accounts created
            if loginFile.readlines() != "":
                for names in loginFile.readlines():
                    print(names)
                    if(names.startswith("Username:")):
                        # Cuts the string to remove the "Username:"
                        uname = names[-9:]
                        print(uname)
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
                print("There are currently no accounts made\nType \"/signup\" to create an account.")
                prompt = input("")
                if prompt == "/signup":
                    sign = signup.SignUp()
                    sign.__init__()
        print("You have been authenticated!!!".upper())


