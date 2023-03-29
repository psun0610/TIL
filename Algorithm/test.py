import sys
input = sys.stdin.readline

n = int(input())
# n의 값 만큼 테이블 생성
dp = [0] * (n + 1)
dp[1] = 1

# 점화식, 피보나치 수열과 유사함
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])