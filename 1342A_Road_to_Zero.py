for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    d = abs(y - x) * a
    print(min((x + y) * a, d + x * b, d + y * b))

    

    