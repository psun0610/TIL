n = int(input())
street = []
street = list(map(int, input().split()))

slope = False
start = 0
size = 0
max_size = 0
for i in range(1, n):
    # 현재 오르막길이 아니라면 i와 i-1을 비교하여 오르막길일 때 start 기록
    if slope is False:
        if street[i-1] < street[i]:
            slope = True
            start = street[i-1]
            size = street[i] - start
            if max_size < size:
                max_size = size
    # 현재 오르막길일때
    else:
        # 오르막길이면
        if street[i-1] < street[i]:
            size = street[i] - start
            # 오르막길의 크기가 이전까지의 최대 오르막길 크기보다 크다면 바꿔줌
            if max_size < size:
                max_size = size
        else:
            # 내리막길이면 slope = false
            slope = False
print(max_size)