n, m = map(int, input().split())
h = {}
for _ in range(m):
    k, v = input().split()
    h[k] = v if len(v) < len(k) else k
a = input().split()
for i in range(n):
    a[i] = h[a[i]]
print(' '.join(a))