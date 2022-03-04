def btk(nums, path=[]):
    if len(ans) == n:
        return
    if not nums:
        ans.append(path)
        return
    for i in range(len(nums)):
        if len(path) >= 2 and path[-1] + path[-2] == nums[i]:
            continue
        btk(nums[:i] + nums[i + 1:], path + [nums[i]])
for _ in range(int(input())):
    n = int(input())
    nums = list(range(1, n + 1))
    ans = []
    btk(nums)
    for a in ans:
        for i in a:
            print(i, end=" ")
        print()
    
