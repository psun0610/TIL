import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan)
while(start <= end):
    mid = (start + end) // 2    # 자를 선 길이
    cnt = 0                     # 몇 개 자를 수 있는 지
    for l in lan:
        cnt += l // mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)