for _ in range(int(input())):
    s = input()
    ans = s[0]
    for i in range(1, len(s) - 1, 2):
        ans += s[i]
    ans += s[-1]
    print(ans)