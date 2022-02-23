import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
*a, d = [int(finput()) for _ in range(5)]
dp = [0] * (d + 1)
for h in a:
    for i in range(h, d + 1, h):
        dp[i] = 1
fprint(str(sum(dp)) + '\n')