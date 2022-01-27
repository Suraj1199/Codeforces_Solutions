n = int(input())
ans = 1
prev = input()
for _ in range(n - 1):
    x = input()
    if x != prev:
        ans += 1
    prev = x
print(ans)
