for _ in range(int(input())):
    n, s = map(int, input().split(" "))
    print(min(n + 1, s // (n ** 2)))