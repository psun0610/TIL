n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]

# 가로로 체크, 세로로 체크해서 둘 중 max값 출력
width = 0
length = 0
for i in range(n):
    if 'X' not in castle[i]:
        width += 1
for i in range(m):
    tmp_matrix = []
    for j in range(n):
        tmp_matrix.append(castle[j][i])
    if 'X' not in tmp_matrix:
        length += 1
print(max(width, length))