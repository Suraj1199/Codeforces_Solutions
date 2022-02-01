t = int(input())
for _ in range(t):
    n = int(input())
    i = 2
    while True:
        q = 2 ** i - 1
        if n % q == 0:
            print(n // q)
            break
        i += 1
    