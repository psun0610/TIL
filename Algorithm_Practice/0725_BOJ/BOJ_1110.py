N = int(input())
while 1:
    # 주어진 수의 가장 오른쪽 자리 num1
    num1 = N % 10
    # 주어진 수의 각 자리 숫자 합의 가장 오른쪽 자리 num2
    tmpN = N
    total = 0
    while tmpN:
        total = tmpN % 10
        tmpN //= 10
    num2 = total % 10
    cycle = 0