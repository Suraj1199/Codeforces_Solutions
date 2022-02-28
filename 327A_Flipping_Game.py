n = int(input())
a = list(map(int, input().split(" ")))
def flip(a, i, j):
    for k in range(i, j + 1):
        a[k] ^= 1
ans = 0
for i in range(n):
    for j in range(i, n):
        flip(a, i, j)
        ans = max(ans, a.count(1))
        flip(a, i, j)
print(ans)