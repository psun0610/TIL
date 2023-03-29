n = int(input())    # 전체 사람의 수 n (정점의 개수)
a_person, b_person = map(int, input().split())  # 촌수를 계산해야 하는 두 사람의 번호
m = int(input())    # 부모 자식들 간의 관계의 개수 m (간선의 개수)
list_ = [[] for _ in range(n + 1)]      # 인접 리스트 만들기
for i in range(m):
    x, y = map(int, input().split())
    list_[x].append(y)
    list_[y].append(x)

stack = []                      # 돌다가 모든 인접요소들을 방문했다면 다시 뒤로 돌아갈 때 필요한 stack 선언
visited = [False] * (n + 1)     # 모든 요소들을 방문했는지 확인할 때 쓸 visited 리스트
chon = [0] * (n + 1)            # a_person과 다른 사람들간의 촌수를 입력할 촌수 리스트
                                # 이 촌수 리스트에서 b_person과의 촌수를 구함

stack.append(a_person)          # a_person을 먼저 방문함
visited[a_person] = True

while stack:
    current = stack.pop()
    
    for adjacency in list_[current]:
        if visited[adjacency] == False:
            visited[adjacency] = True
            stack.append(adjacency)
            chon[adjacency] += chon[current] + 1

if chon[b_person] == 0:         # b_person의 촌수가 0으로 저장돼있다면 a_person과의 촌수가 없는 것이므로 -1을 출력함
    print(-1)
else:
    print(chon[b_person])       # 아니라면 a_person과 b_person의 촌수를 출력함