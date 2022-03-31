for _ in range(int(input())):
    x = int(input())	
    steps = 0
    while steps * (steps + 1) < 2 * x:
        steps += 1
    if steps * (steps + 1) / 2 == x + 1:
        steps += 1
    print(steps)