import sys
# 16. Write a function is_factor(f, n) that passes these tests:
# test(is_factor(3, 12))
# test(not is_factor(5, 12))
# test(is_factor(7, 14))
# test(not is_factor(7, 15))
# test(is_factor(1, 15))
# test(is_factor(15, 15))
# test(not is_factor(25, 15))
# An important role of unit tests is that they can also act as unambiguous “specifications”
# of what is expected. These test cases answer the question Do we treat 1 and 15 as factors
# of 15?


def is_factor(fac, num):
    if num % fac == 0:
        return True
    else:
        return False


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(is_factor(3, 12))
test(not is_factor(5, 12))
test(is_factor(7, 14))
test(not is_factor(7, 15))
test(is_factor(1, 15))
test(is_factor(15, 15))
test(not is_factor(25, 15))