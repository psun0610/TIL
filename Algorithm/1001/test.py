from sys import stdin

S, E, Q = input().strip().split()
S = int("".join(S.split(":"))) # 개강총회를 시작한 시간
E = int("".join(E.split(":"))) # 개강총회를 끝낸 시간
Q = int("".join(Q.split(":"))) # 스트리밍 끝낸 시간
participant = {} # 개강총회 시작 전 채팅 친 사람들
count = 0
while(True):
    line = stdin.readline().strip() # int(input()) 사용 시 발생한 런타임 오류 해결 
    if len(line) < 1: 
        break # 마지막 입력 이후 돌아가는 line을 
    t, _id = line.split()
    t = int("".join(t.split(":")))
    if t <= S: participant[_id] = 1
    elif E <= t <= Q:
        if participant.get(_id) == 1:
            participant[_id] = participant[_id] + 1 
            count += 1
print(count)