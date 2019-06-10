

def count_letters(phrase, letter):
    count = 0
    for char in phrase:
        if char == letter:
            count += 1
    return count

print(count_letters('banana', 'a'))