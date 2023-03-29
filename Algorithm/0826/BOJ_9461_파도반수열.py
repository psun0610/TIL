import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    j = 0
    dp = [1, 1, 1, 2, 2]
    for i in range(5, n):
        dp.append(dp[i-1] + dp[j])
        j += 1
    print(dp[n-1])



import sys
sys.stdin = open('9461_파도반수열.txt')
input = sys.stdin.readline

t = int(input())
# 수열, 숫자의 나열, 삼각형 변의 길이 나열,
# (1,1,1,2,2,3,4,5,7,9) 
# 5번째 + 1번째 = 6번째 
# 6번째 + 2번째 = 7번째
# 7번째 + 3번째 = 8번째
# 8번째 + 4번째 = 9번째
# 9번째 + 5번째 = 10번째
# 10번째 + 6번째 = 11번째 ?인가 ?
for test_case in range(t):
    n = int(input()) # 수열의 n번째 수 구하기 P(n)
    dp = [0,1,1,1,2,2] +[0]*n # 5번째 까지는 고정, 6번째부터 규칙적
    for i in range(6,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])