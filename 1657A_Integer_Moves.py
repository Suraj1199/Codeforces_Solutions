def find(a, b):
    for i in range(a, -1, -1):
        for j in range(b, - 1, - 1):
            r = i ** 2 + b ** 2
            if int(r ** 0.5) ** 2 == r:
                return i, j
    return 0, 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print(0)
        continue
    ans = 0
    while True:
        ans += 1
        x, y = find(a, b)
        if a == x and b == y:
            break
        a, b = x, y
        
    print(ans)
    
