xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Part A

for i in xs:
    print(i)

# Part B

for i in xs:
    print(f'Initial Value:{i}    Value Squared:{i**2}')

# Part C

total = 0
for i in xs:
    total += i

print(f'\n{xs}')
print(f'Total of the list is: {total}')

# Part D


prod_total = 1
for i in xs:
    prod_total *= i

print(f'\n{xs}')
print(f'Product of all integers in the list is: {prod_total}')
