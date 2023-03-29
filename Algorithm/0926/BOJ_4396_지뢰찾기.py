n = int(input())
matrix = [input() for i in range(n)]
open_matrix = [input() for i in range(n)]
answer = [[0] * n for i in range(n)]
mine = False
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for x in range(n):
    for y in range(n):
        if open_matrix[x][y] == 'x':
            if matrix[x][y] == '*':
                mine = True
                continue
            cnt = 0
            for d in delta:
                dx = x + d[0]
                dy = y + d[1]
                if 0 <= dx < n and 0 <= dy < n and matrix[dx][dy] == '*':
                    cnt += 1
            answer[x][y] = cnt
        else:
            answer[x][y] = '.'

for i in range(n):
    for j in range(n):
        if mine and matrix[i][j] == '*':
            print('*', end='')
        else:
            print(answer[i][j], end='')
    print()
