# Import Statements
import signup


class Authenticated:
    def __init__(self,):
        user_auth = False
        pass_auth = False
        username = input("Please enter your Username: ")
        password = input("Please Enter your password: ")
        loginFile = open("names.cred", "r")
        print(loginFile.readlines())
        while user_auth == False or pass_auth == False:
            # Checkes if there are any accounts created
            if loginFile.readlines() != "":
                count = 0
                for names in loginFile.readlines():
                    print(names)
                    if names[count].startswith("Username:"):
                        # Cuts the string to remove the "Username:"
                        uname = names[-9:]
                        print(uname)
                        if username == uname:
                            user_auth = True
                        else:
                            print("username doesn't exist.  Please type \"/signup\" to create an account")
                    elif names[count].startswith("Password:"):
                        pswrd = names[-9:]
                        if password == pswrd:
                            pass_auth = True
                        else:
                            print("Password doesn't match the one on file for", uname)
                    else:
                        print("Something Went wrong!")
                    count += 1
                loginFile.close()
            else:
                # if there are no accounts then prompt to create one
                print("There are currently no accounts made\nType \"/signup\" to create an account.")
                prompt = input("")
                if prompt == "/signup":
                    sign = signup.SignUp()
                    sign.__init__()
        print("You have been authenticated!!!".upper())


