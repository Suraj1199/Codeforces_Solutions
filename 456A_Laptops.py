n = int(input(" "))
laptops = [map(int, input().split(" ")) for i in range(n)]
for p, q in laptops:
    if p != q:
        print("Happy Alex")
        exit()
print("Poor Alex")