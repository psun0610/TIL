from pprint import pprint
n = int(input())
m = int(input())
# 일단 인접 행렬, 인접 리스트 작성해보기
matrix = [[0] * (n+1) for _ in range(n+1)]
list_ = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    
    # 인접 행렬
    matrix[x][y] = 1
    matrix[y][x] = 1

    # 인접 리스트
    list_[x].append(y)
    list_[y].append(x)

pprint(matrix)