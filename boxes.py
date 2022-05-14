a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
i1 = [a1, b1, c1]
i2 = [a2, b2, c2]
i1.sort()
i2.sort()
a1 = i1[0]
b1 = i1[1]
c1 = i1[2]
a2 = i2[0]
b2 = i2[1]
c2 = i2[2]
if a1 == a2 and b1 == b2 and c1 == c2:
    print("Boxes are equal")
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print("The first box is smaller than the second one")
elif a2 <= a1 and b2 <= b1 and c2 <= c1:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
