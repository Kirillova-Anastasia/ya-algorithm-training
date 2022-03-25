n = int(input())
a = [int(x) for x in input().split()]
a.sort()
k = int(input())

for _ in range(k):
    l, r = [int(x) for x in input().split()]
    
    if a[0] > r or a[-1] < l:
        print(0, end = ' ')
        continue
    
    i, j = 0, n - 1
    while j - i > 1:
        t = (i + j) // 2
        if a[t] < l:
            i = t
        else:
            j = t
    res1 = j
    if a[0] >= l:
        res1 = 0
    
    i, j = 0, n - 1
    while j - i > 1:
        t = (i + j) // 2
        if a[t] > r:
            j = t
        else:
            i = t
    res2 = i
    if a[-1] <= r:
        res2 = n - 1
    print(res2 - res1 + 1, end = ' ')
print()