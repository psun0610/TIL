# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98


n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]

for i in range(3):
    for j in range(n - 1):
        tmp_list = []
        for k in range(j + 1, n):               # 비교를 하기 위해서 for 문을 한 번 더 돌림
            if game[j][i] == game[k][i]:        # 비교를 하다가 같은 걸 발견하면
                tmp_list.append(j)              # tmp_list에 j와 k를 넣는다
                tmp_list.append(k)
        tmp_list = list(set(tmp_list))          # tmp_list에 중복된 값을 제거한다
        for tmp in tmp_list:                    # tmp_list에 있는 요소들을
            game[tmp][i] = 0                    # game에 넣고 모두 0으로 만든다
for i in range(n):
    sum_ = 0
    for j in range(3):
        sum_ += game[i][j]
    print(sum_)
