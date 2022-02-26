n = int(input())
a = list(map(int, input().split(" ")))
i, j, k = 0, n - 1, 0
s = [0, 0]
while i <= j:
    if a[i] > a[j]:
        s[k] += a[i]
        i += 1
    else:
        s[k] += a[j]
        j -= 1
    k ^= 1
print(s[0], s[1 ])