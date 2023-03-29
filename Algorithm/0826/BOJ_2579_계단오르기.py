# 한 번에 한 계단, 두 계단 오를 수 있음
# 연속으로 세 계단 밟기 금지
# 마지막 계단은 무조건 밟아야 함
# 최댓값 출력
# import sys
# input = sys.stdin.readline

# n = int(input())
# stairs = [int(input()) for _ in range(n)]

# total = stairs[-1]
# start = -1
# finish = -4
# while 1:
#     if finish + 1 < -n <= start:
#         total += sum(stairs[start-1:-n-1:-1])
#         break
#     list_ = stairs[start:finish:-1]
#     min_ = min(list_)
#     total += (stairs[start-1] if stairs[start-1] != min_ else stairs[start-2])
#     start = finish + list_.index(min_)
#     finish = start - 3
# print(total)

import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
dp = [0] * 301
for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
for i in range(3, n + 1):
    dp[i] = max(stairs[i - 3] + stairs[i - 1] + dp[i - 2],
               stairs[i] + dp[i - 2])
print(dp[n - 1])