def solveSingle(best, other1, other2):
	return str(max(0, max(other1, other2) + 1 - best))

for _ in range(int(input())):
	a, b, c = map(int, input().split())
	print(solveSingle(a, b, c) + ' ' + solveSingle(b, a, c) + ' ' + solveSingle(c, a, b))