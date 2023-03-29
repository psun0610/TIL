import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        current, dis = queue.popleft()
        if current == end:
            return dis
        for adj, d in list_[current]:
            if not visited[adj]:
                visited[adj] = True
                queue.append((adj, dis + d))

n, m = map(int, input().split())
list_ = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, dis = map(int, input().split())
    list_[a].append((b, dis))
    list_[b].append((a, dis))
print(list_)
for i in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))