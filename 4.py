def is_password_good(password):
    if len(password) < 8:
        return False
    else:
        return True
print(is_password_good('aabbCC11OP'))
print(is_password_good('avC1pu'))
