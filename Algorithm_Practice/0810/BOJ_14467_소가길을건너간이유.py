n = int(input())
cow_list = [-1] * 11
cross_cnt = 0
for i in range(n):
    cow, position = map(int, input().split())
    if cow_list[cow] == -1:             # 소의 위치가 한번도 추적되지 않았다면
        cow_list[cow] = position        # 현재 추적된 위치를 업데이트 해준다.
    elif cow_list[cow] != position:     # 현재 추적된 소의 위치와 지난 번 추적의 위치가 다르면
        cross_cnt += 1                  # 길을 건넌 것이므로 count해준다
        cow_list[cow] = position
print(cross_cnt)