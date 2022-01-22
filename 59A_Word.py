s = input()
l, u = 0 , 0
for i in s:
    if i.islower():
        l += 1
    else:
        u += 1
s = s.lower() if l >= u else s.upper()
print(s)