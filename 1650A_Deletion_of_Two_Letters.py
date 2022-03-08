for _ in range(int(input())):
    s = input()
    c = input()
    ans = "NO"
    n = len(s)
    for i in range(n):
        if s[i] == c and i % 2 == 0 and (n - i - 1) % 2 == 0:
            ans = "YES"
            break
    print(ans)

