for _ in range(int(input())):
    n = int(input())
    s = sum(map(int, input().split()))
    if s < n: print(1)
    else: print(s - n)