s = input()
s = s[1:-1].split(", ")
ans = 0
if s != ['']:
    ans = len(set(s))
print(ans)
