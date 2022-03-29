import math
def lcm(s, k):
    res = ""
    while k > 0:
        res += s
        k -= 1
    return res
for _ in range(int(input())):
    s = input()
    t = input()
    n, m = len(s), len(t)
    g = math.gcd(n, m)
    x = lcm(s, m // g)
    y = lcm(t, n // g)
    if x == y:
      print(x)
    else:
      print(-1)