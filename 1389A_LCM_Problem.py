from math import gcd
for _ in range(int(input())):
    x, y = map(int, input().split(" "))
    if 2 * x > y:
        print("-1 -1")
    else:
        print(x, 2 * x)