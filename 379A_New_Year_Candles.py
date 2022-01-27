a, b = map(int, input().split(" "))
def solve(a, b):
    if a < b:
        return 0
    return a // b + solve((a // b) + (a % b), b)
print(a + solve(a, b))