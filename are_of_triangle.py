a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 2
print('{0:.6f}'.format(S))
