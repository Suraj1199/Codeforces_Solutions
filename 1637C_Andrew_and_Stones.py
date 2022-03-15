t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    if max(a[1:-1]) == 1 or (n == 3 and a[1] % 2 == 1):
        print(-1)
        continue
    answer = 0
    for i in range(1, n - 1):
        answer += (a[i] + 1) // 2
    print(answer)
