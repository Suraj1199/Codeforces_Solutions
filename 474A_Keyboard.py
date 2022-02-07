kb = "qwertyuiopasdfghjkl;zxcvbnm,./"
h = {'L' : {kb[i]: kb[i + 1] for i in range(len(kb) - 1)}, 
     'R' : {kb[i]: kb[i - 1] for i in range(1, len(kb))}}
n = input()
s = input()
ans = ''
for c in s:
    ans += h[n][c]
print(ans)