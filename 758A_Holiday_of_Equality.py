n = int(input())
a = [int(i) for i in input().split(" ")]
print(n * max(a) - sum(a))