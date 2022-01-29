a, b = input(), input()
ans = ''
for i, j in zip(a, b):
    if i == j:
        ans += '0'
    else:
        ans += '1' 
print(ans)