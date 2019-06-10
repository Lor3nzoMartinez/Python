

def print_triangle_nums(n):
    sum_acum = 0
    for i in range(1, n+1):
        sum_acum += i
    return sum_acum


for i in range(1, 32):
    print(f'{i}    {print_triangle_nums(i)}')
