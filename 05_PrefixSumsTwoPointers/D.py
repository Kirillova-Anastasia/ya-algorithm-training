s = input()

count = 0
flg = True
for el in s:
    if el == '(':
        count += 1
    elif el == ')':
        count -= 1
    if count < 0:
        flg = False
        break
        
if flg and count == 0:
    print('YES')
else:
    print('NO')