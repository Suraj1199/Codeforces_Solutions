for _ in range(int(input())):
    n = int(input())
    x = y = n // 2
    ans = 0
    for i in range(1, n // 2 + 1):
        ans += i * i * 8
    print(ans)
