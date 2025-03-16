xy = input()
xy = xy.split()

if len(xy) != 2:
    quit()

x = int(xy[0])
y = int(xy[1])

if not (1 <= x <= 6 and 1 <= y <= 6):
    quit()


def prime(sum):
    for num in range(2, sum):
        if sum % num == 0:
            return False
    return True

sum = x + y
print(x, " + ", y, " = ", sum)
print("Lucky Roll" if prime(sum) else "Not a prime number")