a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
a, b, _ = sorted([a, b, c])

if a <= d and b <= e or b <= d and a <= e:
    print("YES")
else:
    print("NO")
