t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = 0
    ans = 0
    for i in s:
        if i == ')':
            if c == 0:
                ans += 1
            else:
                c -= 1
        else:
            c += 1
    print(ans)