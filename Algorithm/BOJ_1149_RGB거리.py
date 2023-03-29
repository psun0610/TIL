import sys
input = sys.stdin.readline

n = int(input())
dp = []
for i in range(n):
    r, g, b = int(input().split())
    dp.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p)