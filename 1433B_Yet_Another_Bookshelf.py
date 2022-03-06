for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    while a[-1] == 0:
        a.pop()
    a.reverse()
    while a[-1] == 0:
        a.pop()
    print(a.count(0))