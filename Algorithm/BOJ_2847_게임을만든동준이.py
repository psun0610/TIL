n = int(input())
game = []
for i in range(n):
    game.append(int(input()))

cnt = 0
for i in range(n-2, -1, -1):
    if game[i+1] <= game[i]:
        cnt += game[i] - game[i+1] + 1
        game[i] -= game[i] - game[i+1] + 1
print(cnt)