# from pprint import pprint
# # 먼저 입력을 이중 리스트로 받음
# matrix = [list(map(int, input().split())) for _ in range(4)]

# # 각 사각형의 크기를 구함
# size = []
# for i in range(4):
#     size.append((matrix[i][2] - matrix[i][0]) * (matrix[i][3] - matrix[i][1]))

# # 리스트를 만들어서 각 사각형에 속하는 모든 좌표를 다 넣음
# list_ = []
# for k in range(4):
#     tmplist = []
#     for i in range(matrix[k][0], matrix[k][2]+1):
#         for j in range(matrix[k][1], matrix[k][3]+1):
#             tmplist.append((i, j))
#     list_.append(tmplist)
# pprint(list_)

# # 각각 사각형에서 겹치는 좌표를 구해서 min과 max를 구해서 부분 사각형의 넓이 뺌
# for i in range(4):
#     tmplist = []
#     for j in range(i+1, 4):
#         tmplist = [i for i in list_[i] if i in list_[j]]
#     print(tmplist)

matrix = [list(map(int, input().split())) for _ in range(4)]
area = [[0]*100 for _ in range(100)]            # 100x100 행렬을 만듬

for mat in matrix:
    for i in range(mat[0], mat[2]):
        for j in range(mat[1], mat[3]):
            area[i][j] = 1
cnt = 0
for a in area:
    cnt += a.count(1)

print(cnt)