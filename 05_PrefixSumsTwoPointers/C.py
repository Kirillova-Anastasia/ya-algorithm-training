n, m = [int(x) for x in input().split()]
x = [[int(x) + 1, i] for i, x in enumerate(input().split())]
y = [[int(x), i + 1] for i, x in enumerate(input().split())]
x.sort(key = lambda x: x[0])
y.sort(key = lambda x: x[0])

answ = [0 for i in range(n)]
y_i = 0
cnt = 0
for num, x_i in x:
    while y_i < len(y) and num > y[y_i][0]:
        y_i += 1
    if y_i >= len(y):
        break
    cnt += 1
    answ[x_i] = y[y_i][1]
    y_i += 1
        
print(cnt)
for el in answ:
    print(el, end = ' ')
print()
    