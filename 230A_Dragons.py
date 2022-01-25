s, n = map(int, input().split(" "))
d = []
for _ in range(n):
    i, j = map(int, input().split(" "))
    d.append((i, j))
for i, j in sorted(d):
    if s > i:
        s += j
    else:
        print("NO")
        exit()
print("YES")
