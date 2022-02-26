n = input()
ans = ''
i = 0
while i < len(n):
    if n[i] == '.':
        ans += '0'
    if n[i] == '-':
        if n[i + 1] == '.':
            ans += '1'
        else:
            ans += '2'
        i += 1
    i += 1
print(ans)