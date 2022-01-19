s = input()
i = 0
for c in s:
    if c == 'hello'[i]:
        i += 1
    if i == 5:
        print('YES')
        exit(0)
print('NO')