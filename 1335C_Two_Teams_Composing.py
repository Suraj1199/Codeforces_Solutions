from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    h = Counter(a)
    mh = max(h, key=h.get)
    print(min(len(h) - (h[mh] <= len(h)), h[mh]))