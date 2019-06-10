import sys

# 2. Write a function day_name that converts an integer number 0 to 6 into the name of a
# # day. Assume day 0 is “Sunday”. Once again, return None if the arguments to the function
# # are not valid. Here are some tests that should pass:
# # test(day_name(3) == "Wednesday")
# # test(day_name(6) == "Saturday")
# # test(day_name(42) == None)


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


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None)




