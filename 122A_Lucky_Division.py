n = int(input())
lucky_nums = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
for l in lucky_nums:
    if l > n:
        break
    elif n % l == 0:
        print("YES")
        exit(0)
print("NO")

