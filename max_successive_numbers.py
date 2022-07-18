n = True

i = 1
i1 = 1
nn = n
while n:
    n = int(input())
    if n == nn:
        i += 1
    if n == 0:
        break
print(i)
