x = int(input())
n = int(input())
price = 0
for i in range(n):
    object, numbers = map(int, input().split())
    price += object * numbers

if price == x:
    print('Yes')
else:
    print('No')