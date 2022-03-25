n = int(input())
a = [int(x) for x in input().split()]

sums = [0]
minx = 0
res = a[0]

for i in range(n):
    sums.append(sums[-1] + a[i])
    minx = min(minx, sums[-2])
    res = max(res, sums[-1] - minx)

print(res)