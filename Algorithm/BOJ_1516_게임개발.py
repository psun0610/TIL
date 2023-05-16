# 틀린 코드

import sys

input = sys.stdin.readline

n = int(input())
build_list = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n
dp[0] = build_list[0][0]
print(dp[0])
for i in range(1, n):
    temp_list = [0]
    for j in range(1, len(build_list[i]) - 1):
        temp_list.append(dp[build_list[i][j] - 1])
    dp[i] = build_list[i][0] + max(temp_list)
    print(dp[i])


# 위상 정렬 사용한 코드
# 위상 정렬
# 1. 진입차수가 0인 노드들을 queue에 넣는다.
# 2. queue에서 pop을 하여 해당 노드와 연결된 노드들을 돌면서 진입차수를 1씩 줄인다.
# 3. 다시 진입차수가 0인 노드를 queue에 넣고 위의 과정을 반복한다.
# *. 이 문제에서는 건물을 동시에 생성할 수 있으므로, 제일 오래 걸리는 미리 지을 건물의 시간과
#    현재 건물의 시간을 더한 값으로 변경한다.
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
answer = [0] * (n + 1)  # 메모이제이션 할 정답 리스트
build_time = [0] * (n + 1)  # 짓는 시간 리스트
graph = [[] for _ in range(n + 1)]  # 위상 정렬에 이용할 간선 리스트
degree = [0] * (n + 1)  # 위상 정렬에 이용할 진입차수 리스트
q = deque()  # 위상 정렬에 이용할 큐

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    build_time[i] = temp[0]
    for j in temp[1:-1]:
        degree[i] += 1
        graph[j].append(i)  # graph[1] = [2, 3, 4]
        # => 2, 3, 4번 건물을 지을 때 1번 건물이 먼저 지어져야 함

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    answer[cur] += build_time[cur]
    for g in graph[cur]:
        degree[g] -= 1
        answer[g] = max(answer[g], answer[cur])
        if degree[g] == 0:
            q.append(g)

print(*answer[1:], sep="\n")
