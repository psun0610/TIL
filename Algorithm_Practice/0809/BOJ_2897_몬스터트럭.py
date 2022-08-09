r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
delta = [(0, 0), (0, 1), (1, 0), (1, 1)]
parking = [0] * 5
for y in range(r):
    for x in range(c):
        breakcnt = 0    # 자동차를 몇 개 부쉈는지 세기 위한 변수 선언
        cnt = 0         # 델타를 모두 반복했는지 확인하기 위한 임시 변수 cnt 선언
        for d in delta:
            ny = y + d[0]
            nx = x + d[1]
            if ny >= r or nx >= c or matrix[ny][nx] == '#':      # 범위를 넘거나 옆이 건물이라면 break
                break
            cnt += 1                        # 델타를 모두 반복했는지를 확인하기 위해서 변수 cnt에 +1 해줌
            if matrix[ny][nx] == 'X':       # 다른 자동차가 있는 자리이면 
                breakcnt += 1               # 다른 차를 몇 개 부쉈는지 셈

        if cnt == 4:                        # 만약에 중간에 break되지 않고 델타를 모두 반복했다면 (cnt가 3이라면)
            parking[breakcnt] += 1          # +1 해줌

# 출력부
for p in parking:
    print(p)
