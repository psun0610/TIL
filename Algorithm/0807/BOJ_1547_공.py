m = int(input())
cups = [1, 2, 3]
for _ in range(m):
    x, y = map(int, input().split())
    tmpx = cups.index(x)
    tmpy = cups.index(y)
    cups[tmpx] = y
    cups[tmpy] = x
print(cups[0])