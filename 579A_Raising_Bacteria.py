n = int(input())
def solve(x):
    if x == 1:
        return 1
    return solve(x // 2) + (x % 2 != 0)
print(solve(n))
