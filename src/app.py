def login(username, password):
    """Basic login function"""
    print("login attemp") # add new
    if username == "admin" and password == "pwd1234":
        return "Success"