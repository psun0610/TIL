code1 = {
    '1': 5000000,
    '2': 3000000,
    '3': 2000000,
    '4': 500000,
    '5': 300000,
    '6': 100000,
    '0': 0
}

code2 = {
    '1': 5120000,
    '2': 2560000,
    '4': 1280000,
    '8': 640000,
    '16': 320000,
    '0': 0
}

T = int(input())
for _ in range(T):
    total = 0
    a, b = map(int, input().split())
    
    if a <= 21:
        prize1 = 0
        sum_ = 0
        while a - sum_ > 0:
            prize1 += 1
            sum_ += prize1
    else:
        prize1 = 0
    
    if b <= 31:
        tmp = 0
        square = 0
        square_sum = 0
        while b - square_sum > 0:
            square = 2**tmp
            square_sum += square
            tmp += 1
    else:
        square = 0
    
    print(code1[str(prize1)] + code2[str(square)])
