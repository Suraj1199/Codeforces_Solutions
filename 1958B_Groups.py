def solve():
    for i in range(4):
        for j in range(i + 1, 5):
            g1 = g2 = no = 0
            for k in range(n):
                g1 += a[k][i]
                g2 += a[k][j]
                no += not (a[k][i] | a[k][j])
            if g1 >= n // 2 and g2 >= n // 2 and not no:
                return 'YES'
    return 'NO'

for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(solve())

