s = input()
a = [0]
for i in range(len(s) - 1):
    a.append(a[-1] + (s[i] == s[i + 1]))
m = int(input())
for _ in range(m):
    l, r = map(int, input().split(" "))
    print(a[r - 1] - a[l - 1])