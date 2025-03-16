numbers_list = input().strip().split()
numbers_list = [int(num) for num in numbers_list]
target = int(input().strip())
results = [0, 0]


if len(numbers_list) < 2 or len(numbers_list) > 100:
    print(results)
    quit()

funded = False
minimum = len(numbers_list)

for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):

        if i == j:
            continue

        if numbers_list[i] + numbers_list[j] == target:
            funded = True

            if i < minimum:
                minimum = i
                results = [i, j]


if not funded:
    results = [0, 0]

print(results)