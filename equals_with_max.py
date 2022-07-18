n = True

max_n = 0
list_n = []
equals = []
i = 0
while n:
    n = int(input())
    list_n.append(n)
    if n == 0:
        max_n = max(list_n)
        for x in list_n:
            if x == max_n:
                i += 1
print(i)
