import sys

sys.stdin = open("_등산로조성.txt")

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    ctmap = [list(map(int, input().split())) for _ in range(n)]
    trail_length = []       # 각각의 등산로 길이를 저장할 리스트, 마지막에 리스트의 max값 출력할 것
    visited = [[False] * n for _ in range(n)]       # 방문 여부를 확인할 리스트
    stack = []      # 반복 중 뒤로 되돌아갈 스택

    # 먼저 리스트의 최댓값을 구함
    ctmap_max = max(map(max, ctmap))
    for i in range(n):
        for j in range(n):
            if ctmap[i][j] != ctmap_max:    # 가장 높은 봉우리에서 시작되어야 하므로 최댓값일 때만 다음을 실행함
                continue
            
            minus = False                   # 딱 한군데에서 산을 1 깎을 수 있다는 조건때문에 만든 부울 변수
            visited[i][j] = True
            stack.append([i, j])

            while stack:
                current = stack.pop()
                for d in delta:
                    ny = i + d[0]
                    nx = i + d[1]
                    if not(0 <= ny < n and 0 <= nx < n):        # 인덱스 범위를 벗어나면 continue
                        continue
                    if ctmap[ny][nx] > ctmap[current[0]][current[1]]:             # (ny, nx)의 값이 현재 값보다 크면 continue
                        continue
                    if visited[ny][nx] == True:                 # 이미 ny와 nx를 방문한 적 있다면 continue
                        continue
                    if minus == False and ctmap[ny][nx] == ctmap[current[0]][current[1]]:       # 아직 산을 깎은 적 없고 현재 값과 다음 값이 같다면
                        visited[ny][nx] = True                  # 방문을 하고 스택을 쌓는다.
                        stack.append([ny, nx])
                        continue
                    elif ctmap[ny][nx] == ctmap[current[0]][current[1]]:          # 현재 값과 같지만 산을 깎은 적이 있다면 continue
                        continue
                    
                    # 위 조건을 제거하고 나면, 인덱스를 벗어나지 않으면서 방문을 한 적이 없고, 현재보다 낮은 지형이다.
                    visited[ny][nx] = True
                    stack.append([ny, nx])

# 순회는 이게 맞는 것 같기도 한데 어떻게 합을 구해야할지..........................잘...............모르게써요................ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ