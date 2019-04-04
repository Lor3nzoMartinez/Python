import math

print("\nSome OOP notes:\n")

# OOP Practice ############

class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


Philo = Dog("Philo",12)
Dani = Dog("Dani", 11)
Emma = Dog("Emma", 13)


def my_function(*args):
    return max(args)


print("The oldest dog is {} years old.".format(
    my_function(Philo.age, Dani.age, Emma.age)), "\n")


# OOP math practice ###########

class BankAccount:

    balance = 0

    def __init__ (self):
        self.balance: 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
print(a.deposit(1500),a.withdraw(750), "\n")


# Minute Converter ##############

minutes = 8911

days = minutes // 1440

hours = (minutes - (days * 1440)) // 60

minute = minutes % 60

print("There are", days, "days", hours, "hours and", minute, "minutes in", minutes, "minutes.\n")

# Input prob
'''
name = input("What should I call you: ")
radius = input("Hello " + name + " what is the radius of your circle: ")
circumference = (2*math.pi*int(radius))

print("Ok", name, "that means the circumference of your circle with a radius of", radius, "is", circumference)
'''

'''
WS ch2_10

You leave for vacation on Friday & return 123 days later.  Use // and % to compute the number of weeks gone and
number of days after Friday that you returned.  What day did you return?
'''

vacation = 123

weeksGone = vacation // 7

daysAfterFriday = vacation % 7

print("If you leave for", vacation, "days after Friday. You have been gone for", weeksGone, "weeks and will return",
      daysAfterFriday, "after friday.\n")

'''
*************************************
WS ch2_11

Use a for loop with range to print out table of numbers for the
Square and cube of integers from 1 to 10.  The first column should have the number, 
the second column will have the square of the number and the third column will have the cube.
**************************************
'''
print("Num", " ", "Squared", " ", "Cubed")
for i in range(1, 11):
    print(i, "   ", (i**2), "       ", (i**3))


sum = 0
for i in range(11,92,2):
    sum = sum + i

print(sum)







