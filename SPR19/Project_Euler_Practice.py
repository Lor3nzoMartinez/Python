# Problem 1


'''
x = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        x += i
        print(i, "+", x, "=", x)

'''

# Problem 2

'''
def FibSequence(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num > 2:
        return FibSequence(num-1) + FibSequence(num-2)

x = 0
for i in range(1, 35):
    if FibSequence(i) % 2 == 0:
        x += FibSequence(i)
        print("X =", x, "I =", i)

print("\nAnswer is:", x)
'''

# Problem 3


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


def find_prime_factors(num):
    for i in range(1, num + 1):
        if is_prime_number(i):
            print(i)

        else:
            return "No primes."


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)


for i in range(716151937, 600_851_475_143):
    x = print_factors(600_851_475_143)
    if is_prime_number(i):
        print(x)

# 716151937
