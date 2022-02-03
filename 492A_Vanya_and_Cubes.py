from re import I


n = int(input())
i = 1
j = 2
h = 0
while n - i >= 0:
    h += 1
    n -= i 
    i += j
    j += 1
print(h)