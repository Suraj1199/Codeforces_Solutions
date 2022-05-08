for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())    
    ax = min(a, x)
    by = min(b, y)
    a -= ax
    x -= ax
    b -= by
    y -= by
    if c >= x + y:
        print("YES")
    else:
        print("NO")