n = int(input())
a = list(map(int, input().split(" ")))
i = a.index(max(a))
j = a[::-1].index(min(a))
print(i + j - (i >= n - j))