n = int(input())
ans = 0
for _ in range(n):
    op = input()
    if op[0] == '+' or op[-1] == '+':
        ans += 1
    else:
        ans -= 1
print(ans)