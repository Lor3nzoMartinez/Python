import sys

# 4. Write a function that helps answer questions like “‘Today is Wednesday. I leave on
# holiday in 19 days time. What day will that be?”’ So the function must take a day name
# and a delta argument — the number of days to add — and should return the resulting
# day name:
# test(day_add("Monday", 4) == "Friday")
# test(day_add("Tuesday", 0) == "Tuesday")
# test(day_add("Tuesday", 14) == "Tuesday")
# test(day_add("Sunday", 100) == "Tuesday")

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def day_name(num):
    if num == 0:
        return 'Sunday'
    elif num == 1:
        return 'Monday'
    elif num == 2:
        return 'Tuesday'
    elif num == 3:
        return 'Wednesday'
    elif num == 4:
        return 'Thursday'
    elif num == 5:
        return 'Friday'
    elif num == 6:
        return 'Saturday'
    else:
        return


def day_num(name):
    if name == 'Sunday':
        return 0
    elif name == 'Monday':
        return 1
    elif name == 'Tuesday':
        return 2
    elif name == 'Wednesday':
        return 3
    elif name == 'Thursday':
        return 4
    elif name == 'Friday':
        return 5
    elif name == 'Saturday':
        return 6
    else:
        return


def day_add(day, deltaDay):
    change = deltaDay % 7
    day = day_num(day)
    return day_name(day + change)


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")