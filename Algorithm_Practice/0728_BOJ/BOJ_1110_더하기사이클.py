num = int(input())
cycle = 0
temp = num

while 1:
    # num의 오른쪽 구하기
    a = str(temp)[-1]

    # 각 자리 수의 합의 오른쪽 구하기
    # list(str)하면 문자열이 하나씩 쪼개져서 리스트에 들어감!
    b = sum(map(int, list(str(temp))))
    b = str(b)[-1]

    # 두 개 더하기
    temp = int(a + b)
    cycle += 1

    if temp == num:
        break
    
print(cycle)