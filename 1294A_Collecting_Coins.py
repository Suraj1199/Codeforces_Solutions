for _ in range(int(input())):
    *a, n = map(int, input().split())
    x = sum([max(a) - i for i in a])
    if n >= x and (n - x) % 3 == 0:
        print('YES')
    else:
        print('NO')
