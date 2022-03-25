a, b, c, d = [int(x) for x in input().split()]
if a < 0:
    a *= -1
    b *= -1
    c *= -1
    d *= -1

x = 1
while a*x*x*x + b*x*x + c*x + d < 0:
    x *= 10
    
y = -1
while a*y*y*y + b*y*y + c*y + d > 0:
    y *= 10

while x - y > 0.0000001:
    t = (x + y) / 2
    if a*t*t*t + b*t*t + c*t + d < 0:
        y = t
    else:
        x = t
print((x+y)/2)