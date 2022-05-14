n = int(input())
h = (n // 60) % 23
m = (n % 60) % 59
s = n % 60
print(h, ':', m, ':', s, sep='')
