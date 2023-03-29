chess = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        # 하얀 칸은 좌표의 합이 짝수임
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
                cnt += 1
print(cnt)