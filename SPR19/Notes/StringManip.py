#
# def up(Word):
#     Ln = len(word)
#     for ndx in range (1 ,Ln):
#         print(Word[:ndx])
#
# def down(Word):
#     Ln = len(Word)
#     for ndx in range (L n -1 ,0 ,-1):
#         print(Word[:ndx])
#
# def updown(Word):
#     up(Word)
#     print(Word)
#     down(Word)

def up(Word):
    x = 0
    while x < len(Word):
        x += 1
        print(Word[:x])

def down(Word):
    x = len(Word)
    while x > 0:
        x -= 1
        print(Word[:x])

def updown(Word):
    up(Word)
    down(Word)

updown('encyclopedia')