mat = [[int(i) for i in input().split(" ")] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
            exit(0)
