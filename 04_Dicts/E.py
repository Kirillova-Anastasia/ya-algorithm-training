n = int(input())
res = {}
translate_num = {}
maxx = 0

for i in range(1,n+1):
    ch = int(input())
    if ch == 0:
        theme = input()
        res[theme] = 1
        translate_num[i] = theme
    else:
        theme = translate_num[ch]
        res[theme] += 1
        translate_num[i] = theme
    _ = input()
    if res[theme] > maxx:
        maxx = res[theme]
    
i = 1
while res[translate_num[i]] != maxx:
    i += 1
print(translate_num[i])