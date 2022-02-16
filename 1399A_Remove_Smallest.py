t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort()
    c = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            c = 1
            break
    if c == 0:
        print("YES")
    else:
        print("NO")
