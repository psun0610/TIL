import sys
input = sys.stdin.readline

# 시간을 모두 분 단위로 바꿔주는 함수
def time_change(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

S, E, Q = input().split()
S = time_change(S)
E = time_change(E)
Q = time_change(Q)
dic = {}
cnt = 0

while 1:
    try:
        time, name = input().split()
        time = time_change(time)
        # 개강총회 시작 시간 전에 입력한 사람
        if time <= S:
            dic[name] = time
        # 개강총회 종료 후 ~ 스트리밍 종료 후에 입력한 사람
        # +
        # 시작 시간 전에 입력한 적 있는 사람
        elif E <= time <= Q and dic.get(name) != None:
            dic.pop(name)
            cnt += 1
    except:
        break
print(cnt)