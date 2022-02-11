from collections import Counter
from math import ceil
n = int(input())
g = [int(i) for i in input().split(" ")]
h = {1: 0, 2: 0, 3: 0, 4:0}
for i in g:
    h[i] += 1
ans = h[4] + h[3]
h[1] -= min(h[3], h[1])
ans += h[2] // 2 + (h[2] % 2 != 0)
h[1] -=  min(h[1], (h[2] % 2 != 0) * 2)
ans += h[1] // 4 + (h[1] % 4 != 0)
print(ans)
