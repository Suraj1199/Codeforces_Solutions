for _ in range(int(input())):
    n = int(input())
    a = set()
    i = 1
    while i * i <= n:
        a.add(i * i)
        i += 1
    i = 1
    while i * i * i <= n:
        a.add(i * i * i)
        i += 1
    print(len(a))
    