for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split(" "))), reverse=True)
    s1 = s2 = 0
    for i in range(n):
        if s1 < s2:
            s1 += a[i]
        else:
            s2 += a[i]
    if s1 == s2:
        print("YES")
    else:
        print("NO")