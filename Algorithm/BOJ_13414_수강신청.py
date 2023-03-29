import sys
input = sys.stdin.readline
k, l = map(int, input().split())
dic = {}
for i in range(l):
    num = input().strip()
    dic[num] = i
ans = sorted(dic.items(), key=lambda x:x[1])
for i in range(k):
    if i >= len(ans):
        break
    print(ans[i][0])