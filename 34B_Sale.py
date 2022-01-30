n, m = map(int, input().split(" "))
a = [int(i) for i in input().split(" ")]
a.sort()
ans = 0
for i in range(m):
    if ans + a[i] < ans:
        ans += a[i]
    else:
        break
    
print(ans * -1)
        