months = ['January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for i in months:
    print(f'One of the months of the year is {i}')


sum_accumulator = 0
for i in range(1, 11):
    sum_accumulator += i
    print(sum_accumulator)

prod_accumulator = 1
for i in range(1, 6):
    prod_accumulator *= i
    print(prod_accumulator)
