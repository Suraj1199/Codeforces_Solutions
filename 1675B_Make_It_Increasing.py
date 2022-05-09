from sys import stdin, stdout
finput = stdin.readline
fprint = stdout.write
def solve(a, n):
    ans = 0
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            continue
        c = len(bin(a[i])) - len(bin(a[i + 1]))
        a[i] //= 2 ** c
        ans += c
        if a[i] >= a[i + 1]:
            a[i] //= 2
            ans += 1
        if a[i] == a[i + 1]:
            return -1
    return ans
for _ in range(int(finput())):
    n = int(finput())
    a = list(map(int, finput().split()))
    fprint(str(solve(a, n)) + '\n')