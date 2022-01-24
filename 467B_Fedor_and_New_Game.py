n, m, k = map(int, input().split(" "))
x = []
for _ in range(m + 1):
    x.append(int(input()))
f = x[-1]
x.pop()
c = 0
for i in x:
    if bin(f ^ i)[2:].count('1') <= k:
        c += 1
print(c)