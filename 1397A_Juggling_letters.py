from collections import Counter
def check(s, n):
    for i in s:
        if s[i] % n != 0:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n = int(input())
    s = Counter()
    for i in range(n):
        s += Counter(input())
    print(check(s, n))

