n = int(input())
m = int(input())
days = (m // n)
if n < m:
    print(days + 1)
elif n > m:
    print(days + 1)
else:
    print(days)
