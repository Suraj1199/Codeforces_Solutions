# from math import round
t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    ans = ((k - 1) % (n - 1)) + n * ((k - 1) // (n - 1)) + 1
    print(ans) 
