n, t = map(int, input().split())
g = list(range(n))
k = 0
for i in map(int, input().split()):
    g[k] += i
    k += 1
i = 0
v = set()
while i < n and i not in v:
    v.add(i)
    i = g[i]
if t - 1 in v:
    print('YES')
else:
    print('NO')