for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    tot = 0
    for i in range(n):
        tot += arr[i] - 1
    
    if tot % 2 == 0:
        print("maomao90")
    else:
        print("errorgorn")