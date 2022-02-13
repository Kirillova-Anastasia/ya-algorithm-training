n = int(input())
sums = {}
for i in range(n):
    d, a = [int(x) for x in input().split()]
    if d not in sums:
        sums[d] = 0
    sums[d] += a
for key in sorted(sums):
    print(key, sums[key])