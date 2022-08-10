n, m = map(int, input().split())
list_ = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    list_[u].append(v)
    list_[v].append(u)

connected_component = 0
stack = []
visited = [False] * (n + 1)

while sum(visited) != n:
    for i in range(1, n + 1):
        if visited[i] == False:
            current = i
            stack.append(current)
            visited[current] = True

            while stack:
                current = stack.pop()
                for next in list_[current]:
                    if visited[next] == False:
                        visited[next] = True
                        stack.append(next)
            connected_component += 1
print(connected_component)