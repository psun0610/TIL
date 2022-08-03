n, m = map(int, input().split())

# 반복문 사용
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 리스트 컴프리헨션
matrix = [list(map(int, input().split())) for _ in range(n)]
