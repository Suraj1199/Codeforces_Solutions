i = 0
dp = []
x = 1
for i in range(1000):
    while x % 3 == 0 or x % 10 == 3:
        x += 1
    dp.append(x)
    x += 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1])
