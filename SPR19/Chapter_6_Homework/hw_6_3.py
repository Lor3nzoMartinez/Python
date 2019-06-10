import sys
# 3. Write the inverse function day_num which is given a day name, and returns its number:
# test(day_num("Friday") == 5)
# test(day_num("Sunday") == 0)
# test(day_num(day_name(3)) == 3)
# test(day_name(day_num("Thursday")) == "Thursday")


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


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")