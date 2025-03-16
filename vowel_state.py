state = 0
string = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

for char in string:
    if char in vowels:
        state += 1

print(state)