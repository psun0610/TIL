import sys

sys.stdin = open("_창용마을무리의개수.txt")

# 연결 요소의 개수랑 완전 똑같음!!
T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    town = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        town[x].append(y)
        town[y].append(x)
    
    stack = []
    visited = [False] * (n + 1)
    cnt = 0
    
    for i in range(1, n + 1):
        if visited[i] == True:
            continue
        stack.append(i)
        visited[i] = True
        cnt += 1

        while stack:
            current = stack.pop()    
            for adj in town[current]:
                if visited[adj] == True:
                    continue
                stack.append(adj)
                visited[adj] = True
    print(f'#{test_case} {cnt}')