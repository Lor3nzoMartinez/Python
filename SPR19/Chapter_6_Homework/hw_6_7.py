import sys
# 7. Write a function to_secs that converts hours, minutes and seconds to a total number
# of seconds. Here are some tests that should pass:
# test(to_secs(2, 30, 10) == 9010)
# test(to_secs(2, 0, 0) == 7200)
# test(to_secs(0, 2, 0) == 120)
# test(to_secs(0, 0, 42) == 42)
# test(to_secs(0, -10, 10) == -590)


def hourToSecs(num):
    num = num * 3600
    return num


def minutesToSecs(num):
    num = num * 60
    return num


def to_secs(H, M, S):
    H = hourToSecs(H)
    M = minutesToSecs(M)
    return H + M + S


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
