n = int(input())
p1, *a1 = map(int, input().split(" "))
p2, *a2 = map(int, input().split(" "))
if len(set(a1) | set(a2)) == n:
    print("I become the guy.")
else:
    print( "Oh, my keyboard!")
