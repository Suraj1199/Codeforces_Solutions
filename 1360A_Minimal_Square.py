for _ in range(int(input())):
    a, b = sorted(map(int, (input().split(" "))))
    if 2 * a < b:
        print(b ** 2)
    else:
        print((2 * a) ** 2)