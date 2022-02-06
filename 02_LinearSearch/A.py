tmp = int(input())
maxx = tmp
cnt = 0
while tmp:
    if tmp > maxx:
        maxx = tmp
        cnt = 1
    elif tmp == maxx:
        cnt += 1
    tmp = int(input())
if maxx:
    print(cnt)