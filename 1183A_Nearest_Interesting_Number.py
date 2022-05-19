def sum(a):
    
    return result
a = int(input())
result = 0
while a > 0:
    result += a % 10
    a //= 10
while result % 4 != 0:
    a += 1
print(a)