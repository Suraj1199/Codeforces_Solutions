t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    if ((n * k) // 2) % k == 0:
        print("YES")
        odd = 1
        even = 2
        for i in range(1, n + 1):
            for j in range(k):
                if i % 2 != 0:
                    print(odd, end=" ")
                    odd += 2
                else:
                    print(even, end=" ")
                    even += 2
            print()
    else:
        print("NO")
