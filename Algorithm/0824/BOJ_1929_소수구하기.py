# 에라토스테네스의 체 이용
import sys
input = sys.stdin.readline
def PrimeNumber(n):
    primes = [False, False] + [True] * (n-1)    # 0부터 n
    
    for i in range(2, n+1):
        if primes[i]:
            j = 2
            while i*j <= n:
                primes[i*j] = False
                j += 1
    return primes

m, n = map(int, input().split())
prime_list = PrimeNumber(n)
for i in range(m, n+1):
    if prime_list[i]:   
        print(i)


# 에라토스테네스의 체 + sqrt로 반복 줄임
import sys
input = sys.stdin.readline
import math

def PrimeNumber(n):
    primes = [False, False] + [True] * (n-1)    # 0부터 n
    
    for i in range(2, int(math.sqrt(n+1))+1):
        if primes[i]:
            j = 2
            while i*j <= n:
                primes[i*j] = False
                j += 1
    return primes
    
m, n = map(int, input().split())
prime_list = PrimeNumber(n)
for i in range(m, n+1):
    if prime_list[i]:
        print(i)