n = input()
if int(n) > 0:
    print(n)
else:
    if n[-1] > n[-2]:
        n = n[:-1]
    else:
        n = n[:-2] + n[-1]
    print(int(n))