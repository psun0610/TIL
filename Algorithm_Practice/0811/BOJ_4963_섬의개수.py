'''
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
'''
# import sys
# sys.stdin = open('input_4936.txt', 'r')

delta = [(-1, 0), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]   # 8방위 델타좌표 저장
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island_map = [list(map(int, input().split())) for _ in range(h)]
    island_cnt = 0
    visited = [[False] * w for _ in range(h)]
    stack = []

    for i in range(h):
        for j in range(w):
            y, x = i, j
            if island_map[y][x] == 1 and visited[y][x] == False:     # 현재 위치가 1이고 방문하지 않았던 것이라면 다음 실행
                stack.append((y, x))                        # stack에 y, x 튜플을 넣음
                visited[y][x] = True                        # y, x를 방문했다고 표시함
                island_cnt += 1                             # 섬을 하나 찾았으므로 +1 해줌
                while len(stack) != 0:
                    stack.pop()                             # stack의 제일 위 요소를 뺌
                    for d in delta:
                        ny = y + d[0]
                        nx = x + d[1]
                        if 0 <= ny < h and 0 <= nx < w and island_map[ny][nx] == 1 and visited[ny][nx] == False:     # 인덱스 밖으로 나가지 않고, 옆이 1이라면, 그리고 방문을 하지 않았다면
                            x, y = nx, ny                          # x, y를 옮겨줌
                            visited[y][x] = True                   # 다음을 방문했다고 표시함
                            stack.append((y, x))                   # stack에 쌓음
                            break
    print(island_cnt)