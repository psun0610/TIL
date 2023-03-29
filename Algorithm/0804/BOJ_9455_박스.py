T = int(input())
for test_case in range(T):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for i in range(m)]

    cnt = 0
    for i in range(n):
        floor = m - 1
        for j in range(m-1, -1, -1):
            if box[j][i] == 1:
                cnt += floor - j
                floor -= 1
    print(cnt)