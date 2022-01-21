k, n, w = map(int, input().split(" "))
borrow = w * (w + 1) // 2 * k - n
print(max(borrow, 0))