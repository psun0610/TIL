import sys
input = sys.stdin.readline

tmplist = []
max_ = 0
while 1:
    try:
        a, b, dis = map(int, input().split())
        if max_ < a:
            max_ = a
        if max_ < b:
            max_ = b
    except:
        break
    tmplist.append((a, b, dis))

# 인접 리스트를 만들어줬음
list_ = [[] for _ in range(max_)]
for a, b, dis in tmplist:
    list_[a].append((b, dis))
    list_[b].append((a, dis))

