n = int(input())
if n % 2:
    print(-1)
else:
    a = []
    for i in range(2, n + 1, 2):
        a.extend([i, i - 1])
    print(' '.join(map(str, a)))