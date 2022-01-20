from bisect import bisect_left
n, m = map(int, input().split(" "))
ans = [0]
for i in range(1, n + 1):
    c, t = map(int, input().split(" "))
    ans.append(ans[-1] + c * t)
mom = map(int, input().split(" "))
for i in mom:
    print(bisect_left(ans, i))