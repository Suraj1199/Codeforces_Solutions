a = list(map(int, input().split(" ")))
m = max(a)
for i in a:
    d = m - i
    if d:
        print(d, end=" ")
print()