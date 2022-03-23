for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print(0)
    else:
        s = (a ** 2 + b ** 2)
        if int(s ** 0.5) ** 2 == s:
            print(1)
        else:
            print(2)
    
