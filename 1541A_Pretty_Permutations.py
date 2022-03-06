for _ in range(int(input())):
    n = int(input())  
    ans = [3, 1, 2] if n % 2 == 1 else []
    for i in range(len(ans) + 1, n + 1, 2):
        ans += [i + 1, i]
    print(' '.join(map(str, ans)))