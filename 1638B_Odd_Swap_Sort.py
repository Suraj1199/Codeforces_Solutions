t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    x = y = 0
    s1 = s2 = True
    for i in a:
        if i % 2:
            s1 &= (x <= i) 
            x = i
        else:
            s2 &= (y <= i) 
            y = i
    if s1 and s2:
        print("Yes")
    else:
        print("No")
