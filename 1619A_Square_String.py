for _ in range(int(input())):
    s = input()    
    ok = True
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            if s[i] != s[i + len(s) // 2]:
                ok = False
    else:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")