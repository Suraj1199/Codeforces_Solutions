t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    for i in range(1, n - 1):
        if a[i] == a[i + 1] and a[i] == a[i - 1]:
            continue
        elif a[i] != a[i + 1] and a[i] != a[i - 1]:
            print(i + 1)
            break
        elif a[i] == a[i + 1]:
            print(i)
            break
        elif a[i] == a[i - 1]:
            print(i + 2)
            break
