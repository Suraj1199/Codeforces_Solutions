n, m = map(int, input().split())
ans = -1
minm = (n  + 1) // 2
for i in range(minm, n + 1):
    if i % m == 0:
        ans = i
        break
print(ans)