a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    (a, c) = (c, a)
if a >= c >= b:
    (a, b, c) = (b, c, a)
if b >= a >= c:
    (a, b, c) = (c, a, b)
if b >= c >= a:
    (a, b, c) = (a, c, b)
if c >= a >= b:
    (a, b, c) = (b, a, c)
if c >= b >= a:
    (a, b, c) = (a, b, c)
print(a, b, c)
