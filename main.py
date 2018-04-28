# import statements
import authentication
import signup

class Main:
    def __init__(self):
        prompt = input("Please type \"/login\" to login. Or \"/signup\" to SignUp >> ")
        if prompt.startswith("/"):
            if prompt.lower() == "/login":
                print("Okay we'll get you logged in")
                username = input("Please enter your Username: ")
                password = input("Please Enter your password: ")
                log = authentication.Authenticated(username, password)
            elif prompt.lower() == "/signup":
                print("Okay we can do that, but you will need super user authorization")
                sign = signup.SignUp()
            else:
                print("I don't understand that command please try something else")
                Main().__init__()
        else:
            print("To begin you need to type a forward-slash.")
            Main().__init__()


Main().__init__()
