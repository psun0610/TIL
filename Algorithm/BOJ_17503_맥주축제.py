import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(k)]
beers.sort(key = lambda x: (x[1], x[0]))    # 도수가 낮은 순으로 정렬함

heap = []
vtotal = 0
ans = 0
for beer in beers:
    # 선호도 더하기
    vtotal += beer[0]
    heapq.heappush(heap, beer[0])
    # 만약 N일을 모두 채웠다면
    if len(heap) == n:
        # 선호도를 다 채웠으면 break
        if vtotal >= m:
            ans = beer[1]
            break
        # 선호도를 못채웠으면
        else:
            # 선호도가 젤 작은 거 뺌
            vtotal -= heapq.heappop(heap)
else:
    ans = -1

print(ans)