n, i, j = [int(x) for x in input().split()]

if i < j:
    i, j = j, i
x = i - j - 1
print(min(x, n-2-x))