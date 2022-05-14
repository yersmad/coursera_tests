n = int(input())
quadratN = n ** 2
while n != 0:
    n = int(input())
    if n ** 2 == n ** 2:
        continue
    quadratN = n ** 2
    print(quadratN)
