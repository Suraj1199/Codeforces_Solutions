for _ in range(int(input())):
    s = input()
    ok = (s[-1]=='B')
    sum = 0
    for it in s:
        if it=='A':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            ok = False
    if ok:
        print("YES")
    else:
        print('NO')