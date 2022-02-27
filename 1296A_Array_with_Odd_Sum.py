for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    o = 0
    for i in a:
        if i % 2 != 0:
            o += 1
    if sum(a) % 2 == 1 or 0 < o < n:
        print("YES")
    else:
        print("NO")
