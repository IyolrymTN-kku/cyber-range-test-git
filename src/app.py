# src/app.py
def login(username, password):
    if username == "admin" and \
    password == "secure_pw": # เปลี่ยน
        return "Login Success"
    return "Login Failed"