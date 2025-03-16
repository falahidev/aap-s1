import math

t = int(input())
numbers = []

for i in range(t):
    numbers.append(int(input()))

def is_perfect_square(n):
    return int(math.sqrt(n)) * int(math.sqrt(n)) == n

def is_fibonacci(n):
    if n < 0:
        return "NO"

    first_case = 5 * (n * n) + 4
    second_case = 5 * (n * n) - 4

    return "YES" if is_perfect_square(first_case) or is_perfect_square(second_case) else "NO"

for n in numbers:
    print(is_fibonacci(n))


