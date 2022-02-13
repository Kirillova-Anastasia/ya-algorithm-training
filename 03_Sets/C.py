a = [int(x) for x in input().split()]

d = {}
for el in a:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1

for el in a:
    if d[el] == 1:
        print(el, end = ' ')
print()
