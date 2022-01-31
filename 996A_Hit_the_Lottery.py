n = int(input())
ans = []
for i in [100, 20, 10, 5, 1]:
    q = n // i
    ans.append(q)
    n -= q * i
print(sum(ans))