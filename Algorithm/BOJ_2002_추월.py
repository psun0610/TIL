import sys
input = sys.stdin.readline

n = int(input())
indic = {}
outdic = {}
cnt = 0
for i in range(n):
    indic[input().strip()] = i
for i in range(n):
    outdic[i] = input().strip()

for i in range(n - 1):
    for j in range(i + 1, n):
        
        if indic[outdic[i]] > indic[outdic[j]]:
            cnt += 1
            break
print(cnt)