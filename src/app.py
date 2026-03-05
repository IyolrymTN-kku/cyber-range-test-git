def login(username, password):
    print("Login attempt detected") # เพิ่ม
    if username == "admin":
        return "Login Success"
    return "Login Failed"