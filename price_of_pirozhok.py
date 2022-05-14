a, b, n = int(input()), int(input()), int(input())
rubles = n * a
cents = n * b
print((rubles + cents) // 100, cents % 100)
