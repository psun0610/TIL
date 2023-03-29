import heapq

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    # heapq.heapify(heap)
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))