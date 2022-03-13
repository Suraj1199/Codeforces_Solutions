dp = ['1', '2']
for i in range(2, 1000, 3):
    dp.append(dp[i-1] + '1')
    dp.append('1' + dp[i])
    dp.append('2' + dp[i - 2] + '2')
for _ in range(int(input())):
    n = int(input())
    print(dp[n - 1])