for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    h = {}
    ans = 0
    for i in range(n):
        x = a[i] - i
        if x in h:
            ans += h[x]
        else:
            h[x] = 0
        h[x] += 1
    print(ans)
