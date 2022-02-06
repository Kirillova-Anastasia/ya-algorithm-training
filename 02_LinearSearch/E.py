n = int(input())
a = [int(x) for x in input().split()]

maxx = a[0]
for i in range(n):
    if a[i] > maxx:
        maxx = a[i]
print(sum(a) - maxx)
    