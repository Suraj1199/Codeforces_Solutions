t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    if n >= 3 or (n == 2 and a[0] == a[1]):
        print("NO")
    else:
        print("YES")
