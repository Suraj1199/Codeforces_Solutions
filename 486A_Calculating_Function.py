n = int(input())
e = n // 2  
o = (n + 1) // 2
esum = e * (e + 1) 
osum = (o * (o + 1)) - o
print(esum - osum)
