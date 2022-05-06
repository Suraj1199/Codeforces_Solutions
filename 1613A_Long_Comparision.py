for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    mn = min(p1, p2)
    p1 -= mn
    p2 -= mn
    if p1 >= 7:
        print(">")
    elif p2 >= 7:
        print("<")
    else:
        for i in range(p1):
            x1 *= 10
        for i in range(p2):
            x2 *= 10;
        if x1 < x2:
            print("<")
        elif x1 > x2:
            print(">")
        else:
            print("=")