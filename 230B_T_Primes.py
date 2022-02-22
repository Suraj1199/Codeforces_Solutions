import io, os, sys
# finput = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
finput = sys.stdin.readline
fprint = sys.stdout.write
from math import sqrt
dp = [True for _ in range(1000001)]
dp[0] = dp[1] = False
i = 2
while i * i < 1000001:
    if dp[i]:
        j = i
        while i * j < 1000001:
            dp[i * j] = False
            j += 1
    i += 1
n = int(finput())
a = list(map(int, finput().split(" ")))
for i in a:
    r = int(sqrt(i))
    if r * r == i and dp[r]:
        fprint("YES\n")
    else:
        fprint("NO\n")