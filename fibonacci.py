import math

t = int(input())
nums = [int(input()) for _ in range(t)]

is_fib = lambda n: "YES" if n >= 0 and (
    (s := 5*n*n) and
    (math.isqrt(s+4)**2 == s+4 or
     math.isqrt(s-4)**2 == s-4)
) else "NO"

print(*map(is_fib, nums), sep='\n')
