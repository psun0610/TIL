T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m+1):
        number = str(i)
        for num in number:
            if num == '0':
                cnt += 1
    print(cnt)