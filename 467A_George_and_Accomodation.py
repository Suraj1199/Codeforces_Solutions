n = int(input())
c = 0
for _ in range(n):
    a, b = map(int, input().split(" "))
    if b - 2 >= a:
        c += 1
print(c)