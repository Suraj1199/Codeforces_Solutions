from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = Counter(map(int, input().split()))
    x = max(a, key=a.get)
    if a[x] >= 3:
        print(x)
    else:
        print(-1)