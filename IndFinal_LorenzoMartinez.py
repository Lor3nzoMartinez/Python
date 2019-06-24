from math import sqrt


# Problem 1


def sum_100():
    ''' I instantiate a sum accumulator and then I loop through 100 ints as I square them and
    add the results to sum_acum '''
    sum_acum = 0
    for i in range(1, 101):
        sum_acum += sqrt(i)
    return sum_acum


print(sum_100())


# Problem 2_a


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_odd_num(start, end):
    list_of_odds = []
    for i in range(start, end+1):
        if is_prime(i):
            list_of_odds.append(str(i))
    return list_of_odds


def find_sum(start, end):
    list_of_odds = find_odd_num(start, end)
    sum_acum = 0
    for i in list_of_odds:
        nested_sum = 0
        for j in range(len(i)):
            nested_sum += int(i[j])
        if nested_sum % 2 == 0:
            sum_acum += nested_sum
    return sum_acum


print(f'\n{find_sum(1000, 2000)}')


# Problem 2_b


def find_prod(start, end):
    list_of_odds = find_odd_num(start, end)
    prod_acum = 1
    for i in list_of_odds:
        if i[2] == '8' and i[3] == '7':
            prod_acum *= int(i)
    return prod_acum


print(f'\n{find_prod(1000, 2000)}')


# Problem 2_c


sum, prod = find_sum(1000, 2000), find_prod(1000, 2000)

print(f'\n{(prod-sum)/sum}')


# Problem 3
from random import randint


def doubles_achieved(dice_1, dice_2):
    if dice_1 == 1 and dice_2 == 1:
        return True
    elif dice_1 == 6 and dice_2 == 6:
        return True
    else:
        return False


def rollin_dubs():
    history = 0
    dice1, dice2 = 0, 0
    dice_history = []
    while not doubles_achieved(dice1, dice2):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        dice_history.append(dice1)
        dice_history.append(dice2)
        history += 2
    return dice_history, history


print(f'\n{rollin_dubs()}')


# Problem 4
from math import pi


def circle_area(R):
    R = pi*R**2
    return R


def show_me_the_table():
    counter = 0.50
    print(f'\nRaduis   |   Area')
    print('------------------')
    while counter < 10.25:
        print("{0:5}    |   {1:5}"
              .format(counter, round(circle_area(counter), 3)))
        counter += 0.25


show_me_the_table()


# # Problem 5
# import turtle
#
# wn = turtle.Screen()
# alex = turtle.Turtle()
#
#
# def chevron():
#
#
