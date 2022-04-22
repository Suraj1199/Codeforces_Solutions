for _ in range(int(input())):
    n = int(input())
    print('Division', end=' ')
    if n >= 1900:
        print(1)
    elif 1600 <= n < 1900:
        print(2)
    elif 1400 <= n < 1600:
        print(3)
    else:
        print(4)