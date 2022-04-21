n = int(input())
ans = []
c = 0
for i in range(n):
    if i >= 2 and 'ab'[c] == ans[i - 2]: 
        c ^= 1
    ans.append('ab'[c])
print(''.join(ans))