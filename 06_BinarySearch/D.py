A, K, B, M, X = [int(x) for x in input().split()]

i, j = 1, X
while j - i > 1:
    t = (i + j) // 2
    X_ = (t - (t // K)) * A
    X_ += (t - (t // M)) * B
    if X_ < X:
        i = t
    else:
        j = t
X_ = (i - (i // K)) * A
X_ += (i - (i // M)) * B
if X_ >= X:
    print(i)
else:
    print(j)