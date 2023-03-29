def dfs():
    visited = [[False] * m] * n
    stack = []
    cnt = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and graph[y][x] == 1:
                cnt += 1
                visited[y][x] = True
                stack.append((y, x))
                while stack:
                    cur = stack.pop()
                    for d in delta:
                        ny = cur[0] + d[0]
                        nx = cur[1] + d[1]
                        if 0 <= ny <= n and 0 <= nx <= m and not visited[ny][nx] and graph[ny][nx] == 1:
                            visited[ny][nx] == True
                            stack.append((ny, nx))
    
    return cnt
                    



T = int(input())
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for test_case in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        
    print(dfs())