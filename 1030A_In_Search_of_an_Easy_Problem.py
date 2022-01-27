n = int(input())
ans = 0
x = [int(i) for i in input().split(" ")]
for i in x:
    ans |= i
if ans:
    print("HARD")
else:
    print("EASY")