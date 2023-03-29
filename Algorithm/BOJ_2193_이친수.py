# 1
# 1개

# 10
# 1개

# 100
# 101
# 2개

# 1000
# 1001
# 1010
# 3개

# 10000
# 10001
# 10010
# 10100
# 10101
# 5개

# 100000
# 100001
# 100010
# 100100
# 100101
# 101000
# 101001
# 101010
# 8개
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 1]
for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n])
