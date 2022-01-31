t = int(input())
def similar(a, b, n):
    a, b, n = str(a), str(b), str(n)
    if len(a) != len(n):
        return b
    if len(b) != len(n):
        return a
    c1 = 0
    for i, j in zip(a, n):
        if i != j:
            c1 += 1
    c2 = 0
    for i, j in zip(b, n):
        if i != j:
            c2 += 1
    return a if c1 < c2 else b
    
for _ in range(t):
    n = int(input())
    q = n // 7
    a = q * 7
    b = (q + 1) * 7
    print(similar(a, b, n))
    