n, x = map(int, input().split())
ans, i = 0, 1
while i * i <= x:
    j = x // i
    if x % i == 0 and j <= n:
        ans += 2 - (i == j)
    i += 1
print(ans)