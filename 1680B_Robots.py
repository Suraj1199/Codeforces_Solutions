for i in range(int(input())):
    n, m = map(int, input().split())
    s = []
    for j in range(n):
        s.append(input())
    minx = 10 ** 9
    miny = 10 ** 9
    for x in range(n):
        for y in range(m):
            if s[x][y] == 'R':
                minx = min(minx, x)
                miny = min(miny, y)
    print('YES' if s[minx][miny] == 'R' else 'NO')