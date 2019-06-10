x = 0


def find_hypot(a, b, c):
    if (a ** 2 + b ** 2 == c ** 2):
        return True
    elif (c ** 2 + b ** 2 == a ** 2):
        return True
    elif (a ** 2 + c ** 2 == b ** 2):
        return True
    else:
        return False


print(find_hypot(15, 25, 20))