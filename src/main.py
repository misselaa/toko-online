def login(username, password):
    if username == "admin" and password == "123":
        return "Login sukses"
    else:
        return "Login gagal"