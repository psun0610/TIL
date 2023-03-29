def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))