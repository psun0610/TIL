import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
teams = [list(map(int, input().split())) for _ in range(n)]
members = list(combinations(list(range(n)), n//2))
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0

# print(members)
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# (1, 2), (3, 4) / (1, 3), (2, 4) / (1, 4), (2, 3)
result = []
for member in range(len(members)//2):  # 조합 수만큼 반복함 근데 뒤엔 반복이니까 반만
    start = 0
    link = 0
    for i in range(0, n//2):   # 팀 하나당 들어갈 멤버 수만큼 반복
        for j in range(n//2):
            print(f'i:{i}/ j:{j}')
            start += teams[members[member][i]][members[member][j]]
            link += teams[members[len(members)-i-1][i]][members[len(members)-j-1][j]]
            print(start, link)
    print(f'result: {start, link})
    print('======')
    result.append(abs(start-link))

print(min(result))