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
# 인접 리스트로 먼저 해보기
from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    ans = []
    stack.append(start)
    visited[start] = True
    while stack:
        cur = stack.pop()
        ans.append(cur)
        for adj in sorted(list_[cur], reverse = True):
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True
    return ans

def BFS(start):
    pass

n, m, v = map(int, input().split())
list_ = [[] for _ in range(n + 1)]
pprint(list_)

for i in range(m):
    x, y = map(int, input().split())
    list_[x].append(y)
    list_[y].append(x)
visited = [False] * (n + 1)
stack = []
pprint(list_)

print(DFS(v))
print(BFS(v))
