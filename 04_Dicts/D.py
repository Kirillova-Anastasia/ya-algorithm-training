votes = []
sum_votes = 0
with open('input.txt', 'r') as f:
    for line in f:
        a = line.split()
        votes.append([' '.join(a[:-1]), int(a[-1])])
        sum_votes += int(a[-1])

i_ch = sum_votes / 450
res = {}
sum_places = 0
log = {}

for key, value in votes:
    res[key] = int(value / i_ch)
    sum_places += res[key]
    frac = (value / i_ch) - res[key]
    if frac not in log:
        log[frac] = []
    log[frac].append([value, key]) 

for frac in sorted(log, reverse=True):
    if sum_places >= 450:
        break
    for v, name in sorted(log[frac], reverse=True):
        res[name] += 1
        sum_places += 1

with open('output.txt', 'w') as f:
    for name, _ in votes:
        f.write(f'{name} {res[name]}\n')