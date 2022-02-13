n = int(input())
s = input()

include_answer = set()
possible_answers = set(range(1,n+1))

while s != 'HELP':
    a = set([int(x) for x in s.split()])
    answer = input()
    s = input()
    
    if answer == 'NO':
        possible_answers -= a
        if include_answer:
            include_answer -= a
    else: #YES
        if include_answer:
            include_answer &= a
        else:
            include_answer = a
        
ans = None
if include_answer:
    ans = include_answer & possible_answers
else:
    ans = possible_answers
    
ans = list(ans)
for el in sorted(ans):
    print(el, end = ' ')
print()