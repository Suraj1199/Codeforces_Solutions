from math import sqrt, ceil
t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    if n % 2 != k % 2 or k ** 2 > n:
        print("NO")
    else:
        print("YES")