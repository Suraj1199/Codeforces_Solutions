s = input()
if len(s) == 1 and s.islower():
    s = s.upper()
elif s.isupper():
    s = s.lower()
elif s[0].islower() and s[1:].isupper():
    s = s[0].upper() + s[1:].lower()
print(s)

