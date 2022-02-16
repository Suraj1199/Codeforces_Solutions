n, k = map(int, input().split(" "))
left = (240 - k)
ans = 0
diff = 5
while ans < n and left - diff >= 0:
    ans += 1
    diff += 5 * (ans + 1)
print(ans)