m, s = map(int, input().split(" "))
if (m > 1 and s == 0) or m * 9 < s:
    print("-1 -1")
    exit()
maxm = '9' * (s // 9) + (str(s % 9) if m - s // 9 > 0 else '') + '0' * (m - s // 9 - 1)
minm = list(maxm[::-1])
if m > 1 and minm[0] == '0': 
    for i in range(m):
        if minm[i] != '0':
            minm[i] = str(int(minm[i]) - 1)
            break
    minm[0] = '1'
minm = ''.join(minm)
print(minm, maxm)


