m = int(input())
qs = []
for i in range(m):
    qs.append(set(input()))

n = int(input())
ss = []
res = []
for i in range(n):
    s = input()
    ss.append(s)
    res.append(0)
    for q in qs:
        flag = True
        for el in q:
            if el not in s:
                flag = False
        if flag:
            res[-1] += 1

maxx = max(res)
for el, r in zip(ss, res):
    if r == maxx:
        print(el)