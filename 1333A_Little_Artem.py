for _ in range(int(input())):
    n, m = map(int, input().split())        
    result = [m * ['B'] for _ in range(n)]
    result[0][0] = 'W'
    for i in range(n):
        print(''.join(result[i]))
    