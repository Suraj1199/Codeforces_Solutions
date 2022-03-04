def solve(s):
    k = []
    for i in s:
        if i in 'rgb':
            k.append(i)
        else:
            if i.lower() not in k:
                return False
    return True
for _ in range(int(input())):
    s = input()
    if solve(s):
        print('YES')
    else:
        print('NO')


    