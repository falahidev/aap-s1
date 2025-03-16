key = input().strip()
count = int(input().strip())
over = False
results = []


def check(key, guess):
    result = [""] * len(guess)
    key_chars = list(key)

    for index, char in enumerate(guess):
        if index < len(key) and char == key[index]:
            result[index] = "G"
            if char in key_chars:
                key_chars.remove(char)

    for index, char in enumerate(guess):
        if result[index] == "":
            if char in key_chars:
                result[index] = "Y"
                key_chars.remove(char)
            else:
                result[index] = "R"

    str_result = "".join(result)

    if str_result == "G" * len(key):
        return str_result, True

    return str_result, False


for i in range(count):
    if over:
        results.append("Game Over")
        continue

    guess = input().strip()
    if len(guess) != len(key):
        results.append("Invalid Length")
    else:
        result, over = check(key, guess)
        results.append(result)

for result in results:
    print(result)