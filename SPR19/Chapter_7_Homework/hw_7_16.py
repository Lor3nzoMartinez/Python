import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def sum_squares(list):
    sum_acum = 0
    for i in range(len(list)):
        sum_acum += list[i]**2
    return sum_acum


test(sum_squares([2, 3, 4]) == 29)

test(sum_squares([]) == 0)

test(sum_squares([2, -3, 4]) == 29)
