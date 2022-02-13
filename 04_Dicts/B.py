res = {}
with open('input.txt', 'r') as f:
    for line in f:
        name, votes = line.split()
        if name not in res:
            res[name] = 0
        res[name] += int(votes)
    
with open('output.txt', 'w') as f:
    for key in sorted(res):
        f.write(f'{key} {res[key]}\n')
    