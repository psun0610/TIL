import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for _ in range(m):
    a = list(map(int, input().split()))
    matrix.append(a)

print(matrix)
