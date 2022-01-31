t = int(input())
for _ in range(t):
    n = input()
    a = n.count('1')
    b = len(n) - a
    if a == b:
        print(a - 1)
    else:
        print(min(a, b))