for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = [False] + [a[i] > a[i + 1] and a[i] > a[i - 1] for i in range(1, n - 1)] + [False]
    ans = sum(b)
    for i in range(1, n - 1):
        if b[i]:
            if i + 2 < n and b[i + 2]:
                a[i + 1] = max(a[i], a[i + 2])
                b[i + 2] = False
                ans -= 1
            else:
                a[i] = max(a[i - 1], a[i + 1])
            b[i] = False
    print(ans)
    for i in a:
        print(i, end=" ")
    print()