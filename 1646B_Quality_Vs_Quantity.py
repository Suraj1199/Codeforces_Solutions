for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort()
    blue, red = sum(a[:2]), a[-1]
    i, j = 2, n - 2
    while i < j and red <= blue:
        red += a[j]
        blue += a[i]
        i += 1
        j -= 1
    if red <= blue:
        print("NO")
    else:
        print("YES")

