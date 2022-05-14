now = int(input())
maxNum = now
while now != 0:
    now = int(input())
    if now != 0 and maxNum < now:
        maxNum = now
print(maxNum)
