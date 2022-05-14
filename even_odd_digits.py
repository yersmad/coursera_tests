a, b, c = int(input()), int(input()), int(input())
if a % 2 == 1 and b % 2 == 0 and c % 2 == 0:
    print("YES")
elif a % 2 == 0 and b % 2 == 1 and c % 2 == 0:
    print("YES")
if a % 2 == 0 and b % 2 == 0 and c % 2 == 1:
    print("YES")
elif a % 2 == 1 and b % 2 == 1 and c % 2 == 0:
    print("YES")
if a % 2 == 1 and b % 2 == 0 and c % 2 == 1:
    print("YES")
elif a % 2 == 0 and b % 2 == 1 and c % 2 == 1:
    print("YES")
else:
    print("NO")
