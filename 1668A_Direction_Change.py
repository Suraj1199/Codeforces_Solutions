for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < m:
        n, m = m, n
    if m == 1 and n >= 3:
        print(-1)
    else:
        print(2 * n - 2 - (n + m) % 2)