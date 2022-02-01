from time import sleep, time
n, m = map(int, input().split(" "))
q = [n]
ans = 0
start = time()
visited = set()
while len(q) > 0:
    size = len(q)
    for _ in range(size):
        node = q.pop(0)
        visited.add(node)
        if node == m:
            print(ans)
            exit()
        if node - 1 > 0 and node - 1 not in visited:
            q.append(node - 1)
        if node * 2 <= 2 * m and node * 2 not in visited:
            q.append(node * 2)
    ans += 1