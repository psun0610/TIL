def fibo(n):
    memo[0] = [1, 0]
    memo[1] = [0, 1]

    if n < 2:
        return memo[n]
    
    for i in range(2, n + 1):
        memo[i][0] = memo[i-1][0] + memo[i-2][0]
        memo[i][1] = memo[i-1][1] + memo[i-2][1]
    
    return memo[n]

T = int(input())
for _ in range(T):
    n = int(input())
    memo = [[0, 0] for _ in range(n + 2)]
    print(*fibo(n))