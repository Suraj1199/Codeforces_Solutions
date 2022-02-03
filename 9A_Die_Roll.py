a, b = map(int, input().split(" "))
num = 6 - max(a, b) + 1
den = 6
def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)
g = gcd(num, den)
num //= g
den //= g
print(f"{num}/{den}")