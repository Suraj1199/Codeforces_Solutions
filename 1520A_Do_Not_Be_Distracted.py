for _ in range(int(input())):
    n = int(input())
    s = input()
    v = set()
    i = 0
    while i < n:
        if s[i] not in v:
            v.add(s[i])
            while i + 1 < n and s[i] == s[i + 1]:
                i += 1
        else:
            break
        i += 1
    if i == n:
        print("YES")
    else:
        print("NO")