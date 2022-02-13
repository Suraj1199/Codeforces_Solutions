from math import ceil
n, m, a, b = map(int, input().split(" "))
c = ceil(b / m)
if c > a:
    print(n * a)
else:
    q = n // m
    print(q * b + min((n - q * m) * a, b))