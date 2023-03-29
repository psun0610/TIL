import sys
input = sys.stdin.readline
n = int(input())
ranks = [int(input()) for i in range(n)]
ranks.sort()

cnt = 0
for i in range(n):
    cnt += abs(ranks[i] - (i+1))
print(cnt)
