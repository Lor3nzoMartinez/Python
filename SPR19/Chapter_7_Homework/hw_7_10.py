import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
