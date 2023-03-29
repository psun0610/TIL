snow_white = []
for i in range(9):                      # 리스트에 입력 받음
    snow_white.append(int(input()))

snow_white.sort()                       # 오름차순으로 정렬을 먼저 함

for a in range(8):                      # 9-1 만큼 반복
    for b in range(a+1, 9):             # a+1에서 8까지 반복
        if snow_white[a] + snow_white[b] == sum(snow_white) - 100:
            snow_white.pop(b)
            snow_white.pop(a)
            break
    if len(snow_white) == 7:
        break

for i in snow_white:
    print(i)
