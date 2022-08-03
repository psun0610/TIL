# 문제 잘못 읽어서.... 가로로 전부 다 더하는 풀이를 써버림,,,,,..........................
# 아까우니까 남길래
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# k = int(input())
# for _ in range(k):
#     sum_ = 0
#     i, j, x, y = map(int, input().split())
#     o = j - 1
#     for l in range(i-1, x):
#         if l == x-1:
#             while o < y:
#                 sum_ += matrix[l][o]
#                 o += 1
#         else:
#             while o < m:
#                 sum_ += matrix[l][o]
#                 o += 1
#             o = 0
#     print(sum_) 

import sys

n, m = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    sum_ = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            sum_ += matrix[a][b]
    print(sum_)