calc = lambda a,b,c: abs(a - b) + abs(a - c) + abs(b - c)	
q = int(input())
for i in range(q):
    a, b, c = map(int, input().split())
    ans = calc(a, b, c)
    for da in range(-1, 2):
        for db in range(-1, 2):
            for dc in range(-1, 2):
                na = a + da
                nb = b + db
                nc = c + dc
                ans = min(ans, calc(na, nb, nc))
    print(ans)