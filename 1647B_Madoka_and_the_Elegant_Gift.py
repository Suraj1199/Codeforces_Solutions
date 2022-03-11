def solve():
    for i in range(n-1):
        for j in range(m-1):
            if a[i][j] + a[i+1][j] + a[i][j+1] + a[i+1][j+1] == 3:
                return "NO"
    return "YES"
for _ in range(int(input())):
    n, m  = map(int, input().split(" "))
    a = []
    for _ in range(n):
        a.append(list(map(int, input())))
    print(solve())
