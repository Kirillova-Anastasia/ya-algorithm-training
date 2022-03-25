s = int(input())
n_a, *a = [int(x) for x in input().split()]
n_b, *b = [int(x) for x in input().split()]
n_c, *c = [int(x) for x in input().split()]

d_a = {}
for i, el in enumerate(a):
    if el not in d_a:
        d_a[el] = []
    d_a[el].append(i)
d_b = {}
for i, el in enumerate(b):
    if el not in d_b:
        d_b[el] = []
    d_b[el].append(i)
d_c = {}
for i, el in enumerate(c):
    if el not in d_c:
        d_c[el] = []
    d_c[el].append(i)

a = sorted(list(set(a)))
b = sorted(list(set(b)))
c = sorted(list(set(c)))

answ = []

i, j, k = 0, 0, len(c) - 1

print(a)
print(b)
print(c)

while i < len(a):
    while k >= 0 and a[i] + b[j] + c[k] > s:
        print(i, j, k, 'greater')
        k -= 1
    k_ = k
    while k_ >= 0 and a[i] + b[j] + c[k_] == s:
        print(i, j, k, 'equal')
        for i_place in d_a[a[i]]:
            for j_place in d_b[b[j]]:
                for k_place in d_c[c[k_]]:
                    answ.append([i_place, j_place, k_place])
        k_ -= 1
    if j == len(b) - 1:
        i += 1
    elif i == len(a) - 1:
        j += 1
    elif b[j] < a[i]:
        j += 1
    elif b[j] == a[i] and b[j+1] < a[j+1]:
        j += 1
    else:
        i += 1
        
print(answ)

answ = [f'{i} {j} {k}' for i,j,k in answ]
if len(answ) == 0:
    print(-1)
else:
    print(min(answ))
    