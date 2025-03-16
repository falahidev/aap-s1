inputs = input().strip().split()

if len(inputs) != 2: quit();

mess = inputs[0]
word = inputs[1]


def check(mess, word):
    index = 0

    for char in mess:
        if char == word[index]:
            index = index + 1
            if index == len(word):
                return "YES"
    return "NO"

print(check(mess, word))