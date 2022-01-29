k, n = map(int, input().split(" "))
a = [int(i) for i in input().split(" ")]
a.sort()
ans = float('inf')
for i in range(n - k + 1):
    x = a[i:i+k]
    ans = min(ans, max(x) - min(x))
print(ans)