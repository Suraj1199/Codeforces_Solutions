for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split(" "))
    L = n * (a - b) 
    R = n * (a + b)
    if R < c - d or c + d < L:
        print("No")
    else:
        print("Yes")

    