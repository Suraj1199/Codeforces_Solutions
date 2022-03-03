for _ in range(int(input())):
    a = list(map(int, input().split(" ")))
    if max(a[:2]) + max(a[2:]) == sum(sorted(a)[2:]):
        print("YES")
    else:
        print("NO")
