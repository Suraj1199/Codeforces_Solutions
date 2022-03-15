from sys import stdin, stdout

MOD = 998244353

ux = []
uy = []
for _ in range(int(stdin.readline())):
	n, m, k, q = map(int, stdin.readline().split())
	while len(ux) < n:
		ux.append(False)
	while len(uy) < m:
		uy.append(False)
	xs = [-1 for i in range(q)]
	ys = [-1 for i in range(q)]
	for i in range(q):
		x, y = map(int, stdin.readline().split())
		xs[i] = x - 1
		ys[i] = y - 1
	cx = 0
	cy = 0
	ans = 1
	for i in range(q - 1, -1, -1):
		fl = False
		if not ux[xs[i]]:
			ux[xs[i]] = True
			cx += 1
			fl = True
		if not uy[ys[i]]:
			uy[ys[i]] = True
			cy += 1
			fl = True
		if fl:
			ans = ans * k % MOD
		if cx == n or cy == m:
			break
	for i in range(q):
		ux[xs[i]] = False
		uy[ys[i]] = False
	stdout.write(str(ans) + "\n")