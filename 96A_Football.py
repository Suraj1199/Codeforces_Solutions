s = input()
i = 0
while i < len(s) - 1:
    c = 0
    if s[i] != s[i + 1]:
        i += 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        i += 1
        c += 1
        
    if c >= 6:
        print("YES")
        exit()
print("NO")