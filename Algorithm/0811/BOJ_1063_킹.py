delta = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}
king, stone, n = input().split()
kingy, kingx = 8 - int(king[1]), ord(king[0]) - 65
stoney, stonex = 8 - int(stone[1]), ord(stone[0]) - 65

for i in range(int(n)):
    move = input()
    ky = delta[move][0] + kingy                     # 킹이 이동할 다음 좌표값을 구함
    kx = delta[move][1] + kingx

    if 0 <= ky < 8 and 0 <= kx < 8:                 # 킹이 인덱스범위를 벗어나지 않는지 확인
        if ky == stoney and kx == stonex:           # 돌 방향으로 움직이면 돌도 같이 이동
            sy = delta[move][0] + stoney
            sx = delta[move][1] + stonex
            if 0 <= sy < 8 and 0 <= sx < 8:         # 돌이 이동할 방향이 인덱스를 벗어나지 않는지 확인
                stoney = sy                         # 돌과 킹을 같이 이동함
                stonex = sx
                kingy = ky
                kingx = kx
        else:                                       # 만약 돌이랑 상관 없는 이동이라면 킹만 이동시킴
            kingy = ky
            kingx = kx

print(f'{chr(kingx + 65)}{8 - kingy}')
print(f'{chr(stonex + 65)}{8 - stoney}')
