import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# BFS
def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for d in delta:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if matrix[ny][nx] == '1':
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

n, m = map(int ,input().split())
matrix = [input().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
BFS()
# pprint(visited)
print(visited[n-1][m-1])