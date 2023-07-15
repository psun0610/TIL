# 1이 있는 칸을 모두 BFS
import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

answer = 0

while queue:
    x, y = queue.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 벗어나면 넘어감
            continue

        if graph[nx][ny] != 0:
            continue

        queue.append([nx, ny])
        graph[nx][ny] = graph[x][y] + 1  # 거리 1 증가
        answer = max(answer, graph[x][y] + 1)

print(answer - 1)
