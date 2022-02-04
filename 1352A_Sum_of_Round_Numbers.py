t = int(input())
for _ in range(t):
    n = input()
    tmp = []
    for i in range(len(n)):
        if n[i] != '0':
            tmp.append(n[i] + (len(n) - i - 1) * '0')
    print(len(tmp))
    for i in tmp:
        print(i, end=" ")
    print()