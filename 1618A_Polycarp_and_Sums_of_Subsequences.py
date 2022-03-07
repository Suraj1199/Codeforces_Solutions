for _ in range(int(input())):
    b = input().split(" ")
    if b[0] + b[1] != b[2]:
        print(' '.join(b[:3]))
    else:
        print(' '.join(b[:2] + [b[4]]))
