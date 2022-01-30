n = int(input())
h = {}
for _ in range(n):
    s = input()
    h[s] = h.get(s, 0) + 1

print(max(h, key=h.get))