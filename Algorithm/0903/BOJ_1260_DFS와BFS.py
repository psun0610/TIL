# 첫째 줄에 DFS, 둘째 줄에 BFS
# 방문할 수 있는 정점이 여러 개인 경우 번호가 작은 것부터 먼저 방문
# 방문할 수 있는 정점이 없다면 종료
# 시작 번호 V
'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    dfs_visited[start] = True
    print(start, end=' ')
    for adj in sorted(graph[start]):
        if not dfs_visited[adj]:
            DFS(adj)
            dfs_visited[adj] = True
    return

def BFS(start):
    queue = deque([start])
    bfs_visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for adj in sorted(graph[cur]):
            if not bfs_visited[adj]:
                queue.append(adj)
                bfs_visited[adj] = True


n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(start)
print()
BFS(start)
