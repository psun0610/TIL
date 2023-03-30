n = int(input())
cnt = 0

max5 = n // 5
for i in range(max5, -1, -1):
    m = n - (5 * i)
    cnt = i
    if m % 3 == 0:
        cnt += m // 3
        print(cnt)
        break
else:
    print(-1)