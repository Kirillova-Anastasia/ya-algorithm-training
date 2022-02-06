d = [int(x) for x in input().split()]
n = len(d)
ans = []

last_m = -1
for i, el in enumerate(d):
    if el == 1:
        if last_m == -1:
            ans.append(n)
        else:
            ans.append(i - last_m)
    elif el == 2:
        last_m = i
        ans.append(-1)
    else:
        ans.append(-1)
        
last_m = -1
for i in range(n-1,-1,-1):
    if d[i] == 1 and last_m != -1:
        ans[i] = min(ans[i], last_m - i)
    elif d[i] == 2:
        last_m = i

print(max(ans))
    