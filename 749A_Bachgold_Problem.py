n = int(input())
ans = ['2'] * (n // 2 - n % 2) + ['3'] * (n % 2)
print(f"{len(ans)}\n{' '.join(ans)}")