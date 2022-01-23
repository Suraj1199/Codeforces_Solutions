n = int(input())
nums = [int(i) for i in input().split(" ")]
for i in range(1, n - 1):
    if nums[i] % 2 != nums[i - 1] % 2  and nums[i] % 2 != nums[i + 1] % 2:
        print(i + 1)
        exit()
    elif nums[i] % 2 != nums[i - 1] % 2:
        print(i)
        exit()
    elif nums[i] % 2 != nums[i + 1] % 2:
        print(i + 2)
        exit()