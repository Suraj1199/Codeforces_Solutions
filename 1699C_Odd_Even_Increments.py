for _ in range(int(input())):
    n = int(input())
    a = [i % 2 for i in map(int, input().split())]
    ans = 'YES'
    for i in range(2, n):
        if a[i] != a[i - 2]:
            ans = 'NO'
            break
    print(ans)
        

