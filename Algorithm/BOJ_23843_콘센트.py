import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
charges = list(map(int, input().split()))
charges.sort(reverse=True)
con = [0] * m   # 콘센트만큼 리스트 만듬
for i in range(n):
    heapq.heappush(con, charges[i] + heapq.heappop(con))
print(max(con))