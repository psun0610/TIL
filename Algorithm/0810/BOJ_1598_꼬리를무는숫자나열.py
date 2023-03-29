a, b = map(int, input().split())

if a % 4 == 0:
    ay = 4
    ax = a // 4
else:
    ay = a % 4
    ax = a // 4 + 1


if b % 4 == 0:
    by = 4
    bx = b // 4
else:
    by = b % 4
    bx = b // 4 + 1

print(abs(ax-bx) + abs(ay-by))