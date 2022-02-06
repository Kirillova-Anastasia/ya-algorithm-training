l, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

ans = []
if l % 2 == 1 and l // 2 in a:
    ans.append(l // 2)
elif l % 2 == 1:
    i = k - 1
    while a[i] > l // 2:
        i -= 1
    ans.append(a[i])
    i = 0
    while a[i] < l // 2:
        i += 1
    ans.append(a[i])
else: # l % 2 == 0
    i = k - 1
    while a[i] > l // 2 - 1:
        i -= 1
    ans.append(a[i])
    i = 0
    while a[i] < l // 2:
        i += 1
    ans.append(a[i])

for el in ans:
    print(el, end = ' ')
print()