n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
dp = [0 for _ in range(n)]
v = set()
for i in range(n - 1, -1, -1):
    v.add(a[i])
    dp[i] = len(v)
for _ in range(m):
    l = int(input())
    print(dp[l - 1])