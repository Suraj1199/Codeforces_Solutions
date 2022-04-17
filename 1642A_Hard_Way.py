for _ in range(int(input())):
    b, a = map(int, input().split())
    d, c = map(int, input().split()) 
    f, e = map(int, input().split())
    ans = 0
    if a == c and e < a: ans = abs(b - d)
    elif c == e and a < c: ans = abs(d - f)
    elif a == e and c < a: ans = abs(b - f)
    print(ans)