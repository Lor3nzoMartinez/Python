
list = [2,4,6,8,10]


def odd_counter(list):
    counter = 0
    for i in range(len(list)):
        if list[i] % 2 != 0:
            counter += 1
    return counter


print(odd_counter(list))
