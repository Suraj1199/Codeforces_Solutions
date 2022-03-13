from sys import stdin, stdout
finput = stdin.readline
fprint = stdout.write
from collections import Counter
for _ in range(int(finput())):
    n, x = map(int, finput().split(" "))
    a = list(map(int, finput().split(" ")))
    c = Counter(a)
    for i in sorted(c):
        if c[i] and i * x in c:
            if c[i] > c[i * x]:
                c[i] -= c[i * x]
                c[i * x] = 0
            else:
                c[i * x] -= c[i]
                c[i] = 0
    ans = sum(c.values())            
    fprint(str(ans)+'\n')
        