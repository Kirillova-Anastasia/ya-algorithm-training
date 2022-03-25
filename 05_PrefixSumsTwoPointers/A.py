n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

sums = [0]
for i in range(n):
    sums.append(sums[-1] + a[i])

for i in range(q):
    l, r = [int(x) for x in input().split()]
    print(sums[r] - sums[l-1])