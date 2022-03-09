N = int(input())
h, a = [], []
for i in range(N):
    hi, ai = map(int, input().split(" "))
    h.append(hi)
    a.append(ai)
ans = 0
for i in range(N):
    for j in range(N):
        if i != j and h[i] == a[j]:
            ans += 1
print(ans)