import sys
input = sys.stdin.readline

n = int(input())
weight_list = list(map(int, input().split()))
weight_list.sort()
dp = [[] for i in range(n)]
dp[0] = list(weight_list[0])

for i in range(1, n):
    for j in range(i):
        dp[i].add()
