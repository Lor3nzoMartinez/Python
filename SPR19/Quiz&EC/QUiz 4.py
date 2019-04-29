
sum_acum = 0

for i in range(200, 1001):
    if i % 17 == 0:
        print(f'{i} + {sum_acum} = {sum_acum + i}')
        sum_acum += i
    elif i % 37 == 0:
        print(f'{i} + {sum_acum} = {sum_acum + i}')
        sum_acum += i
    elif i % 47 == 0:
        print(f'{i} + {sum_acum} = {sum_acum + i}')
        sum_acum += i

print(f'The sum of ints from 200 to 1000 inclusive '
      f'that are div by 17 or by 37 or by 47 is {sum_acum}.')