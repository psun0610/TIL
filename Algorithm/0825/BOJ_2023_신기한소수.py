import math
import sys
input = sys.stdin.readline

n = int(input())
for num in range(10**(n-1)*2, 10**(n-1)*8):

    for i in range(n-1, -1, -1):
        tmp = num // (10 ** i)            # 왼쪽부터 소수 확인
        # j = 100000000
        stop = False
        for j in range(2, int(math.sqrt(tmp))+1):
            if tmp % j == 0:
                stop = True
                break
        if stop:
            break
    else:
        print(num)
