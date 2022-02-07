n = int(input())
s = input()
st = []
for i in s:
    if st and i != st[-1]:
        st.pop()
    else:
        st.append(i)
print(len(st))