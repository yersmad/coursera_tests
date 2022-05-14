n = int(input())
i = 1
sum = 0
while i <= n:
    s = 1 / (i ** 2)
    sum += s
    i = i + 1
print(sum)
