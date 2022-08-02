import heapq
import sys

n = int(input())
xnumbers = []
for _ in range(n):
    xnumbers.append(int(sys.stdin.readline()))

heap = []
for x in xnumbers:
    # x가 0이 아니면 heap에 x 푸쉬
    if x != 0:
        # 구글링함
        # 힙은 앞에 거만 가지고 정렬을 하므로 튜플을 이용하면 됨
        heapq.heappush(heap, (abs(x), x))
    # x가 0이라면
    else:
        # 배열이 비어있지 않다면
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)