import math
def solution(fees, records):
    dict = {}
    answer = []
    for record in records:
        time, car_num, in_out = record.split()
        hour, min = map(int, time.split(':'))
        time = hour * 60 + min              # 분으로 바꿈
        
        if car_num in dict:
            dict[car_num].append(time)
        else:
            dict[car_num] = [time]
            
    tmplist = list(dict.items())
    tmplist.sort(key = lambda x: x[0])      # 차량 번호가 작은 순으로 정렬함
    # tmplist = [(차량번호, [시간, 시간, 시간]), (차량번호, [시간 ...])]
    for tmp in tmplist:
        total = 0
        for i in range(len(tmp[1])):
            if i % 2 == 0:              # 입차 시간만큼 총 누적 시간에서 빼기
                total -= tmp[1][i]
            else:                       # 출차 시간만큼 총 누적 시간에 더하기
                total += tmp[1][i]
        if len(tmp[1]) % 2 == 1:             # 마지막이 입차기록이면 23:59에 출차
            total += (23 * 60 + 59)
        
        # 주차 요금 계산
        if total <= fees[0]:        # 기본 시간보다 적으면
            answer.append(fees[1])  # 기본 요금 청구
        else:
            answer.append(fees[1] + math.ceil((total - fees[0])/ fees[2]) * fees[3])      # 기본 시간보다 크면 단위 요금까지 같이 청구함           
                
    return answer
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(*solution(fees, records))