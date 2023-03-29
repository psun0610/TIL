A, B = map(int, input().split())
data = [0]
for i in range(1, B):
    for j in range(i):
        data.append(i)

print(sum(data[A:B+1]))

# 강사님 코드
data = []
N = 1

# 수열의 길이가 B보다 작을 때까지 수열에 숫자 추가
while len(data) < B:
    # N의 크기만큼 수열 리스트에 N을 추가한다.
    for _ in range(N):
        data.append(N)
    N += 1
print(sum(data))