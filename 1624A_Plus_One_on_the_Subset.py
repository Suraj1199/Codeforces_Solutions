for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    m = max(a)
    ans = 0
    for i in a:
        if i < m:
            d = m - i
            ans += d
            m -= d
    print(ans)