n, k = map(int, input().split(" "))
l = [int(i) for i in input().split(" ")]
ans = 0
for i in l:
    if i <= 0 or i < l[k - 1]:
        break
    ans += 1
print(ans)
