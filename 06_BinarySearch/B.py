n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
queries = [int(x) for x in input().split()]

for q in queries:
    i, j = 0, n - 1
    while j - i > 1:
        t = (i + j) // 2
        if a[t] < q:
            i = t
        else:
            j = t
    if a[i] == q:
        res1 = i + 1
    elif a[j] == q:
        res1 = j + 1
    else:
        print(0, 0)
        continue
    
    i, j = 0, n - 1
    while j - i > 1:
        t = (i + j) // 2
        if a[t] > q:
            j = t
        else:
            i = t
    if a[j] == q:
        res2 = j + 1
    elif a[i] == q:
        res2 = i + 1
    print(res1, res2)