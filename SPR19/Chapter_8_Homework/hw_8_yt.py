# Youtube: https://youtu.be/uW1GPFGkyXo


def word_flip(word):
    word = word[::-1]
    return word


def rev_each_word_in(Sentence):
    prev_counter = 0
    counter = 0
    flipper = ""
    rev_sent = []
    sentence = ""
    for i in range(len(Sentence)):
        if Sentence[i] == " " or i == len(Sentence):
            flipper = Sentence[prev_counter:counter]
            flipper = word_flip(flipper)
            prev_counter = counter + 1
            rev_sent.append(flipper + " ")
        elif Sentence[i] == '.':
            flipper = Sentence[prev_counter:counter]
            flipper = word_flip(flipper)
            prev_counter = counter
            rev_sent.append(flipper)
            rev_sent.append(Sentence[i])
        elif i == len(Sentence)-1:
            flipper = Sentence[prev_counter:i+1]
            flipper = word_flip(flipper)
            prev_counter = counter
            rev_sent.append(flipper)
        counter += 1
    return sentence.join(rev_sent)


print(rev_each_word_in("to be or not to be that is the question."))
print(rev_each_word_in("to be or not to be that is the question"))
