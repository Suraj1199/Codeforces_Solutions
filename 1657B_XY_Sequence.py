for _ in range(int(input())):
    n, b, x, y = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a[i - 1] + x
        if a[i] > b:
            a[i] = a[i - 1] - y
    print(sum(a))
