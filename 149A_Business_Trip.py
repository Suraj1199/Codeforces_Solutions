k = int(input())
a = list(map(int, input().split(" ")))
a.sort(reverse=True)
i = 0
while k > 0 and i < 12:
    k -= a[i]
    i += 1
if k <= 0:
    print(i)
else:
    print(-1)