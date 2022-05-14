n = int(input())
h = (n // 60) % 23
m = (n % 60) % 59
print(h, m)
