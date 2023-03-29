n = int(input())
m = int(input())
list_ = [[] for _ in range(n + 1)]

for i in range(m):
    ny, nx = map(int, input().split())
    list_[ny].append(nx)
    list_[nx].append(ny)

visited = [False] * (n + 1)
stack = []

# 1번이 감염되었으니 1번부터 스택에 넣고 부울 True로 변경
stack.append(1)
visited[1] = True

while stack:                            # while len(stack) != 0 과 같은 거임!!
    current = stack.pop()
    for next in list_[current]:
        if visited[next] == False:
            visited[next] = True
            stack.append(next)

print(sum(visited) - 1)