n = int(input())
k = 1
yes = False
while k <= n:
    if k == n:
        yes = True
    k = k * 2
if yes:
    print('YES')
else:
    print("NO")
