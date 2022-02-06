minput = lambda : map(int, input().split(" "))
def ispalin(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True
t = int(input())
for _ in range(t):
    n, k = minput()
    s = input()
    if ispalin(s) or k == 0:
        print(1)
    else:
        print(2)
