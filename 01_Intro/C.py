d, m, y = [int(x) for x in input().split()]

if d >= 13 or m >= 13 or d == m:
    print(1)
else:
    print(0)