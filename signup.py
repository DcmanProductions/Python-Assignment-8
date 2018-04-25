class SignUp:
    # Username, Password, Super User Password
    def __init__(self, username, password, su):
        credFile = open("names.cred", "w")
        credFile.write("Username:", username, "\nPassword:", password)
        credFile.close()

    def __call__(self, *args, **kwargs):
        print("hello")

