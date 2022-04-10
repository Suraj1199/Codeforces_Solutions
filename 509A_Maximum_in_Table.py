n = int(input())
a = [[0] * n for _ in range(n)]
for i in range(n):
    a[0][i] = a[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
print(a[-1][-1])