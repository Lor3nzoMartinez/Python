import random
#
# # Problem 1)
#
#
# Words = ['The', 'moment', 'a', 'little', 'boy', 'is', 'concerned', 'with', 'which', 'is', 'a', 'jay',
#          'and', 'which', 'is', 'a', 'sparrow', 'he', 'can', 'no', 'longer', 'see', 'the', 'birds',
#          'or', 'hear', 'them', 'sing']
#
#
# def find_position(List):
#     counter = 0
#     case_word = 'birds'
#     for i in range(len(List)):
#         if List[i] == case_word:
#             break
#         counter += 1
#     return counter
#
#
# print(find_position(Words))
#
#
# # Problem 2)
#
#
# Words2 = ['Live', 'in', 'such', 'a', 'way', 'that', 'you', 'would', 'not', 'be', 'ashamed', 'to',
#            'sell', 'your', 'parrot', 'to', 'the', 'town', 'gossip']
#
#
# def sum_list(List):
#     sum_acum = 0
#     case_word = 'parrot'
#     for i in range(len(List)):
#         if List[i] == case_word:
#             print(f'Word skipped: {List[i]}')
#         else:
#             sum_acum += len(List[i])
#     return sum_acum
#
#
# print(sum_list(Words2))


# Problem 3


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def greaterthan(n):
    if n > 45:
        return True
    else:
        return False


def combine_conditionals(n):
    if greaterthan(n) and is_prime(n):
        return True
    else:
        return False


def rollDice():
    sum_acum = 0
    while not combine_conditionals(sum_acum):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        d = random.randint(1, 6)
        e = random.randint(1, 6)
        f = random.randint(1, 6)
        g = random.randint(1, 6)
        h = random.randint(1, 6)
        i = random.randint(1, 6)
        j = random.randint(1, 6)
        sum_acum = a + b + c + d + e + f + g + h + i + j
    return sum_acum


print(rollDice())
