from collections import Counter
n = int(input())
a = list(map(int, input().split()))
h = Counter(a)
print(max(h.values()), len(h))

