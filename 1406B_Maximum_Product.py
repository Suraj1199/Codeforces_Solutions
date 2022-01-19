t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    a.sort()
    p1 = a[0] * a[1] * a[2] * a[3] * a[-1]
    p2 = a[0] * a[1] * a[-3] * a[-2] * a[-1]
    p3 = a[-5] * a[-4] * a[-3] * a[-2] * a[-1]
    ans = max(p1, p2, p3)
    print(ans)