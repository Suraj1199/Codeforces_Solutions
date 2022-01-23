n = int(input())
h = {}
for _ in range(n):
    s = input()
    if s not in h:
        h[s] = 1
        print("OK")
    else:
        print(s + str(h[s]))
        h[s] += 1
