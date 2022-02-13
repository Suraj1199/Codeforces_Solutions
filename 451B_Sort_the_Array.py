n = int(input())
a = list(map(int, input().split(" ")))
i = 0
x = 0
while i < n - 1 and a[i] < a[i + 1]:
    i += 1  
if i == n - 1:
    print("yes\n1 1")
    exit()
j = i
while j < n - 1 and a[j] > a[j + 1]:
    j += 1
if a[:i] + sorted(a[i:j+1]) + a[j+1:] == sorted(a):
    print(f"yes\n{i + 1} {j + 1}")
else:
    print("no")