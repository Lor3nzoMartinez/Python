# Youtube:
# Chapter 2 Exercise 5 Homework

'''
Exercise 5

The formula for computing the final amount if one is earning compound interest is given
on Wikipedia as:

A = P( 1 + (r/n))^(n*t)

P = Initial investment
r = Nominal annual interest rate
n = Number of time interest is compounded a year
t = Number of years

Write a Python program that assigns the principal amount of $10000 to variable P, assign
to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt
the user for the number of years t that the
'''



class interestCalculator:

    def __init__(self):
        self.P = int(input("What is your initial investment: "))
        self.r = float(input('''What is your interest rate? (EX: "0.15" for 15%): '''))
        self.n = int(input("How many times a year will the interest compound: "))
        self.t = float(input('''How many years will your investment be in this account?
        \n(EX: "2.5" for two and a half years): '''))

    def first_paren(self):
        return self.r / self.n

    def second_paren(self):
        return self.first_paren()+1

    def raised_power(self):
        return self.second_paren()**(self.n * self.t)

    def principla_equation(self):
        return self.P*self.raised_power()

    def toString(self):
        print("\nYour initial investment will grow by", round(self.principla_equation() - self.P, 2),
              "\ndollars.", "After", self.t, "years you will have", round(self.principla_equation(), 2),
              "\ndollars in the account.")


calculate = interestCalculator()

calculate.toString()
