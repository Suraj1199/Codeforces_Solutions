n = int(input())
v = [0, 0, 0]
for _ in range(n):
    u = map(int, input().split(" "))
    for i, j in enumerate(u):
        v[i] += j
if v[0] == 0 and v[1] == 0 and v[2] == 0:
    print("YES")
else:
    print("NO")
