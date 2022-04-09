for _ in range(int(input())):
    n = int(input())
    a, b, i = 0, 0, 0
    for x in map(int, input().split()):
        if x % 2 != i % 2:
            if i % 2 == 0:
                a += 1
            else:
                b += 1
        i += 1
    if a != b:
        print(-1)
    else:
        print(a)