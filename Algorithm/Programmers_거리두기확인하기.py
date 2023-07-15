def DFS(place):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                for k in range(8):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if not (0 <= nx < 5 and 0 <= ny < 5):
                        continue
                    if place[ny][nx] == "O":
                        # 대각선 O는 다음 거 볼 필요 없음
                        nnx = nx + dx[k]
                        nny = ny + dy[k]
                        if not (0 <= nnx < 5 and 0 <= nny < 5):
                            continue
                        if place[nny][nnx] != "P":
                            continue
                    elif place[ny][nx] == "X":
                        continue
                    elif place[ny][nx] == "P":
                        # 왼쪽 아래
                        if dx[k] == -1 and dy[k] == 1:
                            if place[i][j - 1] == "X" and place[i + 1][j] == "X":
                                continue
                        # 오른쪽 아래
                        elif dx[k] == 1 and dy[k] == 1:
                            if place[i][j + 1] == "X" and place[i + 1][j] == "X":
                                continue
                        # 왼쪽 위
                        elif dx[k] == -1 and dy[k] == -1:
                            if place[i - 1][j] == "X" and place[i][j - 1] == "X":
                                continue
                        # 오른쪽 위
                        elif dx[k] == 1 and dy[k] == -1:
                            if place[i - 1][j] == "X" and place[i][j + 1] == "X":
                                continue

                    return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(DFS(place))
    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
