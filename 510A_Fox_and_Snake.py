n, m = map(int, input().split(" "))
ans = []
last = True
for i in range(n):
    if i % 2 == 0:
        ans.append('#' * m)
    else:
        if last:
            tmp = '.' * (m - 1) + "#"
            last = False
        else:
            tmp = '#' + '.' * (m - 1)
            last = True
        ans.append(tmp)
print('\n'.join(ans))
        