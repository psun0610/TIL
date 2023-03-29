import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

# bfs
dist = [-1] * (n + 1)
queue = deque([x])
dist[x] = 0
while queue:
    v = queue.popleft()
    for i in road[v]:
        if dist[i] == -1:  # 다음 node가 방문하지 않은 곳이라면
            queue.append(i)
            dist[i] = dist[v] + 1

print(dist)
if k in dist:
    for a in range(1, n + 1):
        if dist[i] == k:
            print(i)
else:
    print(-1)
