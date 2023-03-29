import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

cnt = 1
cur = 0
for i in range(n-1):
    cur += leak[i+1] - leak[i]
    if cur + 1 > l:
        cnt += 1
        cur = 0
print(cnt)