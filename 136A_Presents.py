n = int(input())
a = [int(i) for i in input().split(" ")]
ans = [0 for _ in range(n)]
for i in range(n):
    ans[a[i] - 1] = i + 1
for i in ans:
    print(i, end=" ")
print()