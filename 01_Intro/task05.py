d = int(input())
x, y = [int(x) for x in input().split()]

if x < 0 and y < 0: # third quarter
    print(1)
elif x >= 0 and y < 0: # forth quarter
    if x**2 <= (x-d)**2:
        print(1)
    else:
        print(2)
elif x < 0 and y >= 0: # second quarter
    if y**2 <= (y-d)**2:
        print(1)
    else:
        print(3)
else: # first quarter
    if y <= d - x:
        print(0)
    else:
        dB = (x-d)**2 + y**2
        dC = x**2 + (y-d)**2
        if dB <= dC:
            print(2)
        else:
            print(3)