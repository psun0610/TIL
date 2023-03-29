n, p, q = map(int, input().split())
dic = {0 : 1}

def dp(i):
    if i in dic:
        return dic[i]
    
    return dp(i//p) + dp(i//q)

print(dp(n))