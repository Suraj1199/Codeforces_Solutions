def solve(n):
    if int(n[-1]) % 2 == 0:
        return 0
    elif int(n[0]) % 2 == 0:
        return 1
    for i in n:
        if int(i) % 2 == 0:
            return 2
    return -1
for _ in range(int(input())):
    n = input()
    print(solve(n))
