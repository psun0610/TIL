from pprint import pprint
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, -1]


def bfs(n, m, maps_, visited):
    count = 0
    queue = deque([(1, 1)])
    visited[1][1] = True

    while queue:
        cur = queue.popleft()
        x = cur[0]
        y = cur[1]
        visited[y][x] = True
        count += 1
        pprint(visited)
        for i in range(4):
            adj_x = x + dx[i]
            adj_y = y + dy[i]

            if adj_x > m or adj_x < 1 or adj_y > n or adj_y < 1:
                continue
            if (
                not visited[adj_y][adj_x]
                and maps_[adj_y][adj_x] == 1
            ):
                print("통과", adj_x, adj_y)
                queue.append((adj_x, adj_y))
                visited[adj_y][adj_x] = True
    return count


def solution(maps):
    answer = 0
    n = len(maps[0])  # 가로
    m = len(maps)  # 세로
    print(n, m)
    maps_ = [[0] * (n + 1)]
    for map in maps:
        maps_.append([0] + map)
    pprint(maps_)

    # 상대방 진영에 도착할 수 없다면 -1 return
    if (maps_[n - 1][m] == 0) and (maps_[m - 1][n] == 0):
        return -1

    visited = [[False] * (n + 1) for _ in range(m + 1)]
    return bfs(n, m, maps_, visited)


solution(
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ]
)
