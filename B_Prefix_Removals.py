for _ in range(int(input())):
    s = input()
    h = {}
    for i, c in enumerate(s):
        h[c] = i
    i = len(s) - 1
    for c in h:
        i = min(i, h[c])
    print(s[i:])
