def SecondMax(seq): #len(seq) > 1
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max1, max2

def MinimalOdd(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2:
            continue
        if ans == -1 or seq[i] < ans:
            ans = seq[i]
    return ans

def ShortWords(seq):
    if not seq:
        return ''
    minlen = len(seq[0])
    for word in seq:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    for word in seq:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)

def RLE(s):
    ans, tmp, cnt = [], '', 0
    for el in s:
        if el != tmp:
            if cnt > 1:
                ans.append(str(cnt))
            ans.append(el)
            tmp = el
            cnt = 1
        else:
            cnt += 1
    return ''.join(ans)


# a = [int(x) for x in input().split()]
# print(SecondMax(a))

# a = [int(x) for x in input().split()]
# print(MinimalOdd(a))

# a = [x for x in input().split()]
# print(ShortWords(a))

# print(RLE(input()))
        