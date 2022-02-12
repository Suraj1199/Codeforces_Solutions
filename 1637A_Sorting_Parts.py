t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    sort = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("YES")
            sort = False
            break
    if sort:
        print("NO")