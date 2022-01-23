n = int(input())
a = [int(i) for i in input().split(" ")]
total = sum(a)
a.sort()
r = -1
c, taken, left = 0, 0, total
while taken <= left:
    taken += a[r]
    left -= a[r]
    r -= 1
    c += 1
print(c)