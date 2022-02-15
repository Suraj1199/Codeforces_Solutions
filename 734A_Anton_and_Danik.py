from collections import Counter
n = int(input())
s = Counter(input())
if s['A'] > s['D']:
    print('Anton')
elif  s['A'] < s['D']:
    print('Danik')
else:
    print('Friendship')