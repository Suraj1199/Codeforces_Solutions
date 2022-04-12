for _ in range(int(input())):
    x = int(input())
    ans = []
    sum, last = 0, 9
    while sum < x and last > 0:
        ans.append(min(x - sum, last))
        sum += last
        last -= 1
    if sum < x:
        print(-1)
    else:
        ans.reverse()
        print(''.join(map(str, ans)))