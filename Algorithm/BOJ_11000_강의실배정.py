# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())
# lectures = list(tuple(map(int, input().split())) for _ in range(n))
# lectures.sort()
# heap = [0]
# for i in range(n):
#     for finish in heap:
#         # 만약에 수업 끝나는 시각보다 다음 수업 시작하는 시각이 크거나 같다면
#         # 즉 같은 강의실을 사용할 수 있다면
#         if finish <= lectures[i][0]:
#             # 가장 빨리 끝나는 수업 빼고 다음 수업 집어넣음
#             heapq.heappop(heap)
#             heapq.heappush(heap, lectures[i][1])
#             break
#     # 쓰고 있는 강의실 중에 사용할 수 있는 강의실이 없다면 강의실 하나 더 사용함
#     else:
#         heapq.heappush(heap, lectures[i][1])    # 다음 수업 끝나는 시간을 push 함
# print(len(heap))


import sys
import heapq
input = sys.stdin.readline
n = int(input())
lectures = list(tuple(map(int, input().split())) for _ in range(n))
lectures.sort()
heap = [0]
for i in range(n):
    # 만약에 가장 빨리 수업이 끝나는 시간보다 작으면
    # 즉 같은 강의실을 사용할 수 있다면
    if heap[0] <= lectures[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, lectures[i][1])
    # 쓰고 있는 강의실 중에 사용할 수 있는 강의실이 없다면 강의실 하나 더 사용함
    else:
        heapq.heappush(heap, lectures[i][1])    # 다음 수업 끝나는 시간을 push 함
print(len(heap))
