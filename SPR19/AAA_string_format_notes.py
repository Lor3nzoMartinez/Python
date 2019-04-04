# Note for string manipulation

note = "Note'"
print("\n%s start here: \n" % note)

# This prints out "Hello, John!"
name = "John"
print("Hello, %s! \n" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old.\n" % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s\n" % mylist)

# This is how to pre-format string.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
print("\n")

# String index example
astring = "Hello world!"
print(astring.index("o"))
print("\n")

# String count example
astring = "Hello world!"
print(astring.count("l"))
print("\n")

# Index printing example
astring = "Hello world!"
print(astring[3:7])
print("\n")

# Index printing example with jump
astring = "Hello world!"
print(astring[3:7:2])
print("\n")

# Printing word backwards
astring = "Hello world!"
print(astring[::-1])
print("\n")

# String case formatting
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
print("\n")

# String boolean types
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
print("\n")

# String split
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)




