#myset
setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    if x not in myset[x % setsize]:
        myset[x % setsize].append(x)

def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False

def delete(x):
    for i, now in enumerate(myset[x % setsize]):
        if now == x:
            myself[i] = myself[-1]
            myself.pop()
            return
        
# A+B
def APlusB(seq, x):
    for num in seq:
        if 2*num != x and x - num in seq:
            return True
    return False

# Search in dict with possible misalignment
def check(d, word):
    new_d = set(d)
    for el in d:
        for i in range(len(el)):
            new_d.add(el[:i] + el[i+1:])
    return word in new_d
