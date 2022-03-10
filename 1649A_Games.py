for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    l, r = 0, n - 1
    while r >= 0 and a[r] == 1:
        r -= 1
    while l < n and a[l] == 1: 
        l += 1
    if l > r:
        print(0)
    else:
        print(r - l + 2)