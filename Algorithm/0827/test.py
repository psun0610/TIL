n = 2137
for i in range(3, n):
    if n % i == 0:
        print('no')
        break
else:
    print('yes')