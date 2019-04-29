# Define student and attributes

student = {'name': 'John', 'age': 25, 'classes': ['Math', 'CompSci']}

# Update dictionary  entry name and age

student.update({'name': 'Jane', 'age': 21})

# Removes value from dictionary and allows for later use if assigned.

age = student.pop('age')

# Delete value from dictionary

#del student['age']

# Assigning a new key

student['phone'] = '5555555'

# Print specified attribute

print(student['name'])
print(student['classes'])

# Gets key value

print(student.get('name'))
print(age)

# Get number of entries in dictionary

print(len(student))

# Print keys from dictionary

print(student.keys())

# Print values from dictionary

print(student.values())

# print both values and keys

print(student.items())

# Not assigned returns None

print(student.get('phone'))

# Specify reply when not found

print(student.get('phone', 'Not Found'))

# Loop through values in dict

for key, value in student.items():
    print(key, value)
