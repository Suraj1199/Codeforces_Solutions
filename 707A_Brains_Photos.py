n, m = map(int, input().split(" "))
color = False
for i in range(n):
    for j in input().split(" "):
        if j not in 'BWG':
            color = True
if not color:
    print('#Black&White')
else:
    print('#Color')

