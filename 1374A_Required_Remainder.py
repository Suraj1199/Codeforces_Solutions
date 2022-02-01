t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split(" "))
    r = n % x
    if r >= y:
        print(n - (r - y))
    else:
        print(n - x + (y - r))