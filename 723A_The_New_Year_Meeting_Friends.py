a, b, c = map(int, input().split(" "))
ac = abs(c - a)
bc = abs(c - b)
ba = abs(a - b)
print(min(ac + bc, ba + bc, ac + ba))