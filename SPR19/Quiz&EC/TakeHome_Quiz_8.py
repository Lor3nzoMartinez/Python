
alphabet = 'abcdefghijklmnopqrstuvwxyz'
Upper_alpahbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Problem 1


def f(x):
    x = x**2
    return x-10


print('Problem 1:')
for x in range(-2, 3):
    print(x, f(x))


# Problem 2


def value_of_L(letter):
    counter = 1
    letter = letter.lower()
    for i in alphabet:
        if i == letter:
            break
        counter += 1
    answer = f(counter)
    return answer


print('\nProblem 2:')
for letter in 'amtw':
    print(letter, 'has the value of', value_of_L(letter))


# Problem 3


def value_of_W(word):
    sum_acum = 0
    for l in word:
        sum_acum += value_of_L(l)
    return sum_acum


print('\nProblem 3:')
for word in ['abe', 'mop', 'zap']:
    print(word, 'has value', value_of_W(word))


# Problem 4


def value_of_W_1(word):
    sum_acum = 0
    for l in word:
        sum_acum += value_of_L(l)
    return sum_acum


print('\nProblem 4:')
for word in ['Abe', 'mOp', 'zaP']:
    print(word, 'has value', value_of_W_1(word))


# Problem 5

def reformation(sentence):
    all_letters = []
    new_S = ''
    for i in range(len(sentence)):
        for j in alphabet+Upper_alpahbet:
            if sentence[i] == j:
                all_letters.append(sentence[i])
    return new_S.join(all_letters)


def value_of_S(sentence):
    sentence = reformation(sentence)
    return value_of_W_1(sentence)


sent = '''Excellence is an art won by training and habituation. We do not act rightly because

we have virtue or excellence, but we rather have those because we have acted rightly.

We are what we repeatedly do. Excellence, then, is not an act but a habit.'''

print('\nProblem 5:')
print(sent, '\n\nhas value:', value_of_S(sent))
