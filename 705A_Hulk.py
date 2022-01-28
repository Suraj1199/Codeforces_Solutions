n = int(input())
ans = []
for i in range(1, n + 1):
    if i % 2 != 0:
        ans.append("I hate")
    else:
        ans.append("I love")
print(' that '.join(ans), 'it')