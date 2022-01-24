import math
t = int(input())

def solve(n):
    minm = n
    for i in range(2, min(k + 1, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            if n // i <= k and i <= minm:
                return i
            else:
                minm = n // i
    return minm

for _ in range(t):
    n, k = map(int, input().split(" "))
    if n <= k:
        print(1)
    else:
        print(solve(n))

    