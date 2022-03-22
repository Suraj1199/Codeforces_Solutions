def ispalin(s):
    n = len(s)
    for i in range(n // 2 + 1):
        if s[i] != s[n - i - 1]:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    tmp = ''
    for i in s:
        tmp += i
        if len(tmp) > 1 and (tmp == '()' or ispalin(tmp)):
            tmp = ''
            ans += 1
    print(ans, len(tmp))
