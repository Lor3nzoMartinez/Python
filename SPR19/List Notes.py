nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ex1 and Ex2 do same thing:

# Ex1:
# my_list = []
# for i in nums:
#     my_list.append(i)
# print(my_list)

# Ex2:
# my_list = [n for n in nums]
# print(my_list)

# Writes squares to list with comprehension
# my_list = [n*n for n in nums]
# print(my_list)

# Using map + lambda
# my_list = map(lambda n: n*n, nums)
# print(my_list)

# Assign only even numbers with list comprehension
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)
#
# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# Assign 1234 to each instance of abcd (EX: (a,1) (a,2))
# my_list = [(letter, num) for letter in 'abcd' for num in (1, 5)]
# print(my_list)

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spider man']

# Create a dict{'name': 'hero'} for each name, hero in zip(name, heros)
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)


def reverse(x):
    output_len = len(x)
    output = [None] * output_len
    output_index = output_len - 1
    for c in x:
        output[output_index] = c
        output_index -= 1

    return ''.join(output)


print(reverse("catch"))

