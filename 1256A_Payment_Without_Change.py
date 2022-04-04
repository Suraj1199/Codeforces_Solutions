for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
    if s - min(s // n, a) * n <= b:
        print('YES')
    else:
        print('NO') 