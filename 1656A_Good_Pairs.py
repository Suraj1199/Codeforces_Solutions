for _ in range(int(input())):
    n = int(input())
    minv = 1e9+1
    maxv = -1	
    for i, a in enumerate(map(int, input().split())):
        if a > maxv:
            maxi = i+1
            maxv = a
        if a < minv:
            mini = i+1
            minv =  a
    print(mini, maxi)