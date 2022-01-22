n = int(input())
cap, ans = 0, 0
for _ in range(n):
    a, b = map(int, input().split(" "))
    cap = cap - a + b
    ans = max(ans, cap)
print(ans)