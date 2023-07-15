n, m = map(int, input().split())

if n == 1 or m == 1:
    print(1)

elif n < 3:
    result = 1 + (m - 1) // 2
    if result < 4:
        print(result)
    else:
        print(4)

else:
    if m <= 4:
        print(m)
    elif 4 < m < 7:
        print(4)
    else:
        print(m - 2)
