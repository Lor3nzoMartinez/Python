

def number_of_the_day(n):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    counter = 0
    for i in days:
        if counter == n:
            return i
        counter += 1


for i in range(7):
    print(f'The number {i} is {number_of_the_day(i)} in a week')