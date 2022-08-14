m, n = map(int, input().split())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
turn_index = 0
x, y = 0, 0
for i in range(n):
    command, num = input().split()
    num = int(num)
    if command == 'MOVE':                   # MOVE 일 때
        nx = delta[turn_index][0] * num
        ny = delta[turn_index][1] * num
        if 0 <= x + nx <= m and 0 <= y + ny <= m:
            x += nx
            y += ny
        else:
            print(-1)
            break
    else:
        if num == 0:                        # TURN 0 일 때
            turn_index = (turn_index + 1) % 4
        else:                               # TURN 1 일 때
            turn_index = (turn_index - 1) % 4

else:
    print(x, y)
