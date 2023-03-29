# 런타임 에러,,
# while문에 max(trading) != trading[0] ===> 런타임 에러
'''T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    trading = list(map(int, input().split()))
    profit = 0          # 총 이익을 계산할 변수, 정답
    while trading and max(trading) != trading[0]:           # 리스트가 비지 않고 max값이 0번 인덱스에 있지 않을 경우 반복
        max_ = max(trading)
        purchase = 0    # 물건을 산 총 가격
        numbers = 0     # 사들인 물건의 개수
        for i in range(0, trading.index(max_)):
            purchase += trading[i]
            numbers += 1
        profit += max_ * numbers - purchase           # 이득 본 게 얼만지 계산
        trading = trading[trading.index(max_)+1:]     # 현재 max값의 뒤부터 마지막까지 리스트 슬라이싱
    
    print(f'#{test_case} {profit}')
'''
# 반례
# 4 1 1 1 3

# ==========================================
# 정답
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    trading = list(map(int, input().split()))
    profit = 0          # 총 이익을 계산할 변수, 정답
    while trading:           # 리스트가 비지 않을 경우 반복
        max_ = max(trading)
        purchase = 0    # 물건을 산 총 가격
        numbers = 0     # 사들인 물건의 개수
        for i in range(0, trading.index(max_)):
            purchase += trading[i]
            numbers += 1
        profit += max_ * numbers - purchase           # 이득 본 게 얼만지 계산
        trading = trading[trading.index(max_)+1:]     # 현재 max값의 뒤부터 마지막까지 리스트 슬라이싱
    
    print(f'#{test_case} {profit}')