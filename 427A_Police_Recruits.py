n = int(input())
a = list(map(int, input().split()))
ans = x = 0
for i in a:
    if x + i < 0:
        ans += 1
    else:
        x += i
print(ans)