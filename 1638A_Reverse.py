t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    if a[0] != 1:
        i = a.index(1)
        a = a[:i + 1][::-1] + a[i + 1:]
    else:
        i = 0
        while i < n - 1 and a[i + 1] - a[i] == 1:
              i += 1
        if i != n - 1: 
            j = a.index(a[i] + 1)
            a = a[:i+1] + a[i+1:j+1][::-1] + a[j+1:]
    for x in a:
        print(x, end=" ")
    print()