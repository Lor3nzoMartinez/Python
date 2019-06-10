left = 3
sleeps = 137


def day_of_week(n):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    counter = 0
    for i in days:
        if n == counter:
            return i
        counter += 1


def day_of_week_returned(day_left, days_gone):
    result = days_gone % 7
    result = result + day_left
    if(result > 6):
        result = result - 7
    return (day_of_week(result))

# print(day_of_week(left), 137 % 7)
print(day_of_week_returned(left, sleeps))

