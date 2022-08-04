n = int(input())
matrix = [list(input()) for _ in range(n)]

width = 0
length = 0

for i in range(n):
    wcnt = 0
    lcnt = 0
    for j in range(n):                  # 가로 먼저 세기
        if matrix[i][j] == '.':         # .을 만나면 wcnt를 하나 더함
            wcnt += 1
        elif matrix[i][j] == 'X':       # X를 만나면
            if wcnt >= 2:               # wcnt가 2이상이면 누울 자리가 충분한 것이므로
                width += 1              # 가로 누울 수 있는 자리가 하나 더 있다는 뜻으로 +1 해줌
                wcnt = 0                # wcnt = 0 으로 초기화 해줌
            else:                       # 만약 .이 2미만이라면 wcnt = 0 으로 초기화만 해줌
                wcnt = 0                
        if wcnt >= 2 and j == n-1:      # 끝까지 세었을 때 X가 없이 벽을 만났을 때 wcnt가 2 이상이면 자리 개수를 +1 해줌
            width += 1
        
        
        if matrix[j][i] == '.':         # 세로 세기
            lcnt += 1
        elif matrix[j][i] == 'X':
            if lcnt >= 2:
                length += 1
                lcnt = 0
            else:
                lcnt = 0
        if lcnt >= 2 and j == n-1:
            length += 1
print(width, length)