

alphabet = 'abcdefghijklmnopqrstuvwxyz'
Upper_alpahbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Problem 8_1


def numeric_value_ofL(letter):
    counter = 1
    letter = letter.lower()
    for i in alphabet:
        if i == letter:
            break
        counter += 1
    answer = counter
    return answer


# Problem 8_2


def numeric_value_of(word):
    sum_acum = 0
    for l in word:
        sum_acum += numeric_value_ofL(l)
    return sum_acum


# Problem 8_3


# def reformation(sentence):
#     all_letters = []
#     new_S = ''
#     for i in range(len(sentence)):
#         for j in alphabet+Upper_alpahbet:
#             if sentence[i] == j:
#                 all_letters.append(sentence[i])
#     return new_S.join(all_letters)
#
#
# def value_of_S(sentence):
#     sentence = reformation(sentence)
#     return numeric_value_of(sentence)


# Problem 8_4


# def up(word):
#     up = ''
#     for i in word:
#         up += i
#         print(up)
#
#
# def down(word):
#     count = len(word)
#     for i in range(1, 3):
#         print(word[0:count - i])
#
#
# up('dog')
# down('dog')


# Problem 8_5


def count_words(sent):
    count = 1
    letters, word = -1, []
    for i in sent:
        if i == ' ':
            count += 1
            word.append(letters)
        letters = letters + 1
    return count, word


def words_grab(sent):
    amt_wrds, slices = count_words(sent)
    place_holder = 0
    for i in slices:
        print(sent[place_holder:i+1])
        place_holder = i + 2

words_grab('cats dos meska treska washad milos timphe.')






