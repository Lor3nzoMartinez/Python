import sys

odds = [1, 3, 5, 7, 9, 10]
evens = [2, 4, 6, 8, 10]
mixed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def sum_evens(list):
    sum_acum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            break
        sum_acum += list[i]
    if sum_acum == 0:
        sum_acum = 'No odds in list'
    return sum_acum


test(sum_evens(odds) == 'No evens in list')
test(sum_evens(evens) == 30)
test(sum_evens(mixed) == 30)
