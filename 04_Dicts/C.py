analyse = {}
with open('input.txt', 'r') as f:
    for line in f:
        s = line.split()
        for word in s:
            if word not in analyse:
                analyse[word] = 0
            analyse[word] += 1
            
reverse_analyse = {}
for key, value in analyse.items():
    if value not in reverse_analyse:
        reverse_analyse[value] = []
    reverse_analyse[value].append(key)
    
with open('output.txt', 'w') as f:
    for key in sorted(reverse_analyse, reverse=True):
        for el in sorted(reverse_analyse[key]):
            f.write(f'{el}\n')
  