m, n = map(int, input().strip().split(" "))
if m % 2 == 0 and n % 2 == 0:
    ans = m * n // 2
elif m % 2 == 0:
    ans = (m * (n - 1)) // 2 + m // 2
elif n % 2 == 0:
    ans = ((m - 1) * n) // 2 + n // 2
else:
    ans = ((m - 1) * (n - 1)) // 2 + m // 2 + n // 2
print(ans)
