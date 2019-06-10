import random


# Problem 1

# def ratioVtoNV(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowels_count = 0
#     counter = 0
#     for i in vowels:
#         for j in word:
#             if i == j:
#                 vowels_count += 1
#     counter = len(word) - vowels_count
#     return vowels_count / counter
#
#
# for i in ['the', 'theory', 'hawaii']:
#     print(ratioVtoNV(i))


# Problem 2


def coinToss():
    if random.random() > 0.5:
        return 1    # Heads
    else:
        return 0    # Tails


def coinTossUntil5Heads():
    counter = 0
    record = []
    while counter < 5:
        coinTosses = coinToss()
        if coinTosses == 1:
            record.append(coinTosses)
            counter += 1
        else:
            record.append(coinTosses)
            counter = 0
    return record


# print(coinTossUntil5Heads())


# Problem 3


def format_record(record):
    record = record
    counter = 0
    x, y = 0, 0
    for i in record:
        if record[counter] == 1:
            x += 1  # Heads
        else:
            y += 1  # Tails
        counter += 1
    return counter, x, y


times, heads, tails = format_record(coinTossUntil5Heads())

print(f'The coin was tossed {times} times. Heads & tails '
      f'were obtained {round((tails/times) * 100 , 3)}% and '
      f'{round((heads/times) * 100, 3)}% of time.')


