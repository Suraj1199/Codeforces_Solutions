from bisect import bisect
n = int(input())
a = [int(i) for i in input().split(" ")]
a.sort()
m = int(input())
for _ in range(m):
    q = int(input())
    i = bisect(a, q)
    print(i)