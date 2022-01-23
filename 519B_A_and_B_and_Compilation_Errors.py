n = int(input())
s1 = [int(i) for i in input().split(" ")]
s2 = [int(i) for i in input().split(" ")]
s3 = [int(i) for i in input().split(" ")]

print(sum(s1) - sum(s2))
print(sum(s2) - sum(s3))