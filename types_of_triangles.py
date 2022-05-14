a, b, c = int(input()), int(input()), int(input())
if a ** 2 + b ** 2 < c ** 2:
    print("obtuse")
if a ** 2 + b ** 2 > c ** 2:
    print("acute")
elif a ** 2 + b ** 2 == c ** 2:
    print("right")
else:
    print("impossible")
