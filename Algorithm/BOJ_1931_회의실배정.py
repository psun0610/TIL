import sys
input = sys.stdin.readline

n = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(n)]
# 회의가 끝나는 시각으로 정렬
meeting_list.sort(key = lambda x: (x[1], x[0]))

current = meeting_list[0]
cnt = 1

# range 0부터 하면 틀렸습니다 뜸!
# 시작 시간과 끝나는 시간이 같을 수 있기 때문에 첫 번째 요소가 중복되어 세어지기 때문
for i in range(1, n):
    if meeting_list[i][0] >= current[1]:
        current = meeting_list[i]
        cnt += 1
print(cnt)