a, b = map(int, input().split(" "))
d = min(a, b)
print(d, (a - d) // 2 + (b - d) // 2)