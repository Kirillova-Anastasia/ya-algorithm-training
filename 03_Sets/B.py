a = [int(x) for x in input().split()]
s = set()
for el in a:
    if el in s:
        print('YES')
    else:
        print('NO')
        s.add(el)