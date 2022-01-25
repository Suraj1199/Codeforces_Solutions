s = input()
s = s.replace("WUB", ".")
i = 0
ans = []
while i < len(s):
    word = ''
    while i < len(s) and s[i] != '.':
        word += s[i]
        i += 1
    if word != '':
        ans.append(word)
    i += 1
print(" ".join(ans))
    
