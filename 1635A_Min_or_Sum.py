for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    ans = a[0]
    for i in range(1, n):
        ans |= a[i]
    print(ans)