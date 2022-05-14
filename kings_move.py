a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
if a1 + 1 == a2 and b1 + 1 == b2 or \
        a1 - 1 == a2 and b1 - 1 == b2 or \
        a1 - 1 == a2 and b1 + 1 == b2 or \
        a1 + 1 == a2 and b1 - 1 == b2 or \
        a1 + 2 == a2 and b1 - 2 == b2 or \
        a1 - 2 == a2 and b1 + 2 == b2:
    print("YES")
elif a1 == a2 and b1 == b2:
    print("YES")
else:
    print("NO")
