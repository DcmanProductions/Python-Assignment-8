import authentication
class SignUp:
    # Username, Password, Super User Password
    def __init__(self):
        credFile = open("names.cred", "w")
        username = input("Please type a desired username: ")
        password = input("Please type your password: ")
        super_user = input("Please enter the Super User Password (hint: toor): ")
        credFile.write("Username:" + username)
        credFile.write("Password:" + password)
        print("Account saved as", username, password)
        credFile.close()


