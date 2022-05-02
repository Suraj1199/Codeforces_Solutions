t = int(input())
for i in range(t):
    n, r, b = map(int, input().split())
    p = r % (b + 1)
    y = ""
    for j in range(int(r / (b + 1))):
        y = y + "R"
    ans = ""
    for i in range(b + 1):
        if i > 0:
            ans = ans + "B"
        ans = ans + y
        if p > 0:
            ans = ans + "R"
            p = p - 1
    print(ans)