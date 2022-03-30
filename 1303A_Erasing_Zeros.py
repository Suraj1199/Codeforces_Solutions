for _ in range(int(input())):
    s = input()
    for k, c in enumerate(s):
        if c == '1':
            break
    ans = t = 0
    for i in range(k + 1, len(s)):
        if s[i] == '0':
            t += 1
        else:
            ans += t
            t = 0
    print(ans)