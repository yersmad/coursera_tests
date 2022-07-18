n = True

list_n = []
max_n = []
max2_n = []
while n:
    n = int(input())
    list_n.append(n)
    if n == 0:
        list_n.remove(max(list_n))
        max2_n = max(list_n)
print(max2_n)
