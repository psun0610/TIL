# omok = [list(map(int, input().split())) for __ in range(19)]

# # 가로, 세로, 오른쪽 아래, 왼쪽 아래
# delta = [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)],
#         [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
#         [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
#         [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5)]]
# i, j = 0, 0
# cnt = 0

# for i in range(19):
#     for j in range(19):
#         status = omok[i][j]
#         if status != 0:                 # 현재 위치에 돌이 있다면 반복문 시작
#             for y in range(4):          # 델타의 네방향을 하나씩 검사함
#                 cnt = 0
#                 x = 0
#                 while cnt < 4:                      # 델타 리스트의 좌표값들을 반복함
#                     ny = i + delta[y][x][0]             # x좌표
#                     nx = j + delta[y][x][1]             # y좌표
#                     x += 1
#                     if nx < 19 and ny < 19 and omok[ny][nx] == status:        # x, y 좌표가 9 미만이어야 하고, 현재 위치의 돌과 그 다음 위치의 돌이 같은 지 확인함
#                         cnt += 1        # 같다면 cnt + 1 해줌
#                     else:
#                         break

#         if cnt >= 4:
#             break
#     if cnt >= 4:
#         break
# if cnt != 4:        # cnt가 4가 아니면 (6목이거나 반복문을 다 돌았음에도 오목이 없다면)
#     status = 0      # 상태를 0

# print(status)
# if status != 0:     # 상태가 0이 아니면 (오목이면)
#     print(i+1, j+1) # 좌표를 출력함 (인덱스 값에 + 1 해줘야 함)

# ===========================================================================

def omokgame():
    for y in range(19):
        for x in range(19):
            if omok[y][x]:
                for d in delta:
                    ny = y + d[0]
                    nx = x + d[1]
                    cnt = 1
                    if not(0 <= ny < 19 and 0 <= nx < 19):
                        continue
                    while 0 <= ny < 19 and 0 <= nx < 19 and omok[ny][nx] == omok[y][x]:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= (y - d[0]) < 19 and 0 <= (x - d[1]) < 19 and omok[y - d[0]][x - d[1]] == omok[y][x]:
                                break
                            if 0 <= (ny + d[0]) < 19 and 0 <= (nx + d[1]) < 19 and omok[ny + d[0]][nx + d[1]] == omok[y][x]:
                                break
                            return omok[y][x], y + 1, x + 1
                        ny += d[0]
                        nx += d[1]
    return 0, 0, 0

omok = [list(map(int, input().split())) for _ in range(19)]

# 가로, 세로, 오른쪽 아래, 오른쪽 위
delta =[[0, 1], [1, 0], [1, 1], [-1, 1]]
color, y, x = omokgame()
if not color:
    print(0)
else:
    print(color)
    print(y, x)