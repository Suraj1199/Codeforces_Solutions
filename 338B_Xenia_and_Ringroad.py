n, m = map(int, input().split())
a = map(int, input().split())
ans, p = 0, 1
for i in a:
    p = i - p
    if p < 0:
        p += n
    ans += p
    p = i
print(ans)