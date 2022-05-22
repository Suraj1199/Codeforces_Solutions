from collections import Counter
for _ in range(int(input())):
    n = int(input())
    d = Counter(map(int, input().split()))
    cnt = 0
    for i in d:
        cnt += 1 
    for k in range(1, n + 1):
        print(max(k, cnt))