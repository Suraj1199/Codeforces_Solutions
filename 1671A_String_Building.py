for _ in range(int(input())):
    s = input() + '.'
    grp, tmp = [], ''
    for i in range(len(s) - 1):
        tmp += s[i]
        if s[i + 1] != s[i]:
            grp.append(tmp)
            tmp = ''
    ans = 'YES'
    for i in map(len, grp):
        if i == 1:
            ans = 'NO'
            break
    print(ans)
