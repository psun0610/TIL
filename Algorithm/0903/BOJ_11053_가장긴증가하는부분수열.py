n = int(input())
a = list(map(int, input().split()))

cnt = 0
cur = 0
a.sort()
for i in range(n):
    if cur < a[i]:
        cnt += 1
        cur = a[i]

print(cnt)