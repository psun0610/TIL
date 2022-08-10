n = int(input())    # 전체 사람의 수 n (정점의 개수)
a_person, b_person = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())    # 부모 자식들 간의 관계의 개수 m (간선의 개수)
list_ = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    list_[x].append(y)

stack = []
visited = [False] * (n + 1)
a_appear, b_appear = False, False

while sum(visited) != n:        # 모든 요소들을 방문할 때까지 반복함
    for i in range(1, n + 1):   # 1부터 n까지 반복하는데
        if visited[i] == False: # 만약 i를 방문하지 않았다면 실행
            current = i         # 현재 값을 i로 둠
            visited[i] = True
            stack.append(i)
            a_count, b_count = 0, 0

            while stack:
                current = stack.pop()
                if a_appear == False:
                    a_count += 1
                if b_appear == False:
                    b_count += 1
                
                for next in list_[current]:
                    if visited[next] == False:
                        visited[next] = True
                        stack.append(next)
                        if next == a_person:
                            a_apear = True
                        if next == b_person:
                            b_apear = True
                        
if a_count == 0 or b_count == 0:
    print(-1)
else:
    print(a_count + b_count - 2)