import sys
from collections import deque
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]  # 8방위 델타

# BFS
def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == False:
                if matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

while 1:
    w, h = map(int, input().split())
    if not w + h:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for x in range(h):
        for y in range(w):
            if matrix[x][y] == 1 and not visited[x][y]:
                BFS(x, y)
                cnt += 1
    print(cnt)