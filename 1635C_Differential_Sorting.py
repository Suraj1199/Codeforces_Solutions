for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    i = n - 2
    while  i >= 0 and a[i] <= a[i + 1]:
        i -= 1
    if i == n - 2 or (i >= 0 and a[-1] < 0):
        print(-1)
        continue

    print(i + 1)
    j = i
    while j >= 0:
        print(j + 1, i + 2, n)
        j -= 1