m = c = 0
for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    if a > b:
        m += 1
    elif a < b:
        c += 1
if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")