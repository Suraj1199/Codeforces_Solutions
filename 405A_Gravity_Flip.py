n = int(input())
a = [int(i) for i in input().split(" ")]
for i in sorted(a):
    print(i, end=" ")
print()