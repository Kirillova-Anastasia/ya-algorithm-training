n, k = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
# with open('017', 'r') as f:
#     lines = [line for line in f]
#     n, k = [int(x) for x in lines[0].split()]
#     x = [int(x) for x in lines[1].split()]

x.sort()

i, j = 0, x[-1] - x[0]

while j - i > 1:
    t = (i + j) // 2
    k_ = k
    last = -1
    while k_ > 0 and last < n - 1:
        last += 1
        edge = x[last] + t
        k_ -= 1
        while last < n - 1 and x[last] <= edge:
            last += 1
        if x[last] > edge:
            last -= 1
    if last == n - 1: # was able to cover
        j = t
    else:
        i = t
        
k_ = k
last = -1
while k_ > 0 and last < n - 1:
    last += 1
    edge = x[last] + i
    k_ -= 1
    while last < n - 1 and x[last] <= edge:
        last += 1
    if x[last] > edge:
        last -= 1
if last == n - 1: # was able to cover
    print(i)
else:
    print(j)