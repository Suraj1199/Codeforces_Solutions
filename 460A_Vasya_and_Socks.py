n, m = map(int, input().split(" "))
def solve(n, m):
    if n < m:
        return n
    return (n // m) * m + solve(n // m + (n % m), m)
print(solve(n, m))
