import sys
input = sys.stdin.readline

n = int(input())
color_list = []
for i in range(n):
    color_list.append(list(map(int, input().split())))

dp = []
dp.append([color_list[0][0], color_list[0][1], color_list[0][2]])
for i in range(1, n):
    temp = []
    temp.append(color_list[i][0] + min(dp[i-1][1], dp[i-1][2]))
    temp.append(color_list[i][1] + min(dp[i-1][0], dp[i-1][2]))
    temp.append(color_list[i][2] + min(dp[i-1][0], dp[i-1][1]))
    dp.append(temp)

print(min(dp[n-1]))