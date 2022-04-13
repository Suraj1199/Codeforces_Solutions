for _ in range(int(input())):
    x = input()
    dig = ord(x[0]) - ord('0') - 1
    l = len(x)
    print(dig * 10 + l * (l + 1) // 2)