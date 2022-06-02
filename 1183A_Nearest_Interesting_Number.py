x = int(input())
while True:
    s, n = 0, x
    while n > 0:
        s += n % 10
        n //= 10
    if s % 4 == 0:
        break
    x += 1
print(x)