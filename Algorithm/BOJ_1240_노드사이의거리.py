import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end, graph):
    queue = deque([(start, 0)])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(1, n):
    a, b, dis = map(int, input().split())
    graph[a].append((b, dis))
    graph[b].append((a, dis))

for i in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b, graph))
