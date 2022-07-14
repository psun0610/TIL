# 부모님과 함께 놀러간 영일이는
# 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
# (잉어, 붕어, 용 등 여러 가지가 적혀있다.)

# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h, w = map(int, input().split())
mylist = [[0 for j in range(w+1)] for i in range(h+1)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            mylist[x][y+j] = 1
    else:
        for j in range(l):
            mylist[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(mylist[i][j], end=' ')
    print()
