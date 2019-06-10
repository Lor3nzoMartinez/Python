xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


def grades(n):
    if n >= 75:
        print('First')
    elif n > 75 or n >= 70:
        print('Upper Second')
    elif n > 70 or n >= 60:
        print('Second')
    elif n > 60 or n >= 50:
        print('Third')
    elif n > 50 or n >= 45:
        print('F1 Supp')
    elif n > 45 or n >= 40:
        print('F2')
    elif n < 40:
        print('F3')
    else:
        return False


for n in xs:
    grades(n)