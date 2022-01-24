n = int(input())
a = [int(i) for i in input().split(" ")]
a.append(0)
l = 1
ans = 0
for i in range(n):
    if a[i] <= a[i + 1]:
        l += 1
    else:
        ans = max(ans, l)
        l = 1
print(ans)
