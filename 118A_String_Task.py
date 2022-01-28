n = input()
n = n.lower()
ans = ''
for i in n:
    if i not in 'aeiouy':
        ans += '.' + i
print(ans)