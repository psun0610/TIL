import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 각 자리까지의 가장 긴 수열의 길이 저장할 dp 리스트
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))