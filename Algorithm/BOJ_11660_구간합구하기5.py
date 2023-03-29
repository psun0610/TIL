import sys
from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# pprint(matrix)

# 누적합 배열 만들기
sum_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_matrix[i][j] = (
            matrix[i - 1][j - 1]
            + sum_matrix[i - 1][j]
            + sum_matrix[i][j - 1]
            - sum_matrix[i - 1][j - 1]
        )
# pprint(sum_matrix)

# 구간합 구하기
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = (
        sum_matrix[x2][y2]
        - sum_matrix[x1 - 1][y2]
        - sum_matrix[x2][y1 - 1]
        + sum_matrix[x1 - 1][y1 - 1]
    )
    print(answer)
