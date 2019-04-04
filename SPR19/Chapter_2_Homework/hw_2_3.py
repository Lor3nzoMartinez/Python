# Chapter 2 Exercise 3 homework

# For loop that returns the sum of 1 to 5 squared\
x = 0
for i in range(1,6):
    print(i, "squared +", x, "=")
    x += i ** 2
    print(x, "\n")

print("Sum of 1 through 5 squared is %s" % x)
