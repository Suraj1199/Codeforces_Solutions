n, m, a = map(int, input().split(" "))
ans = (n // a + 1) if n % a != 0 else n // a
ans *= (m // a + 1) if m % a != 0 else m // a
print(ans)
