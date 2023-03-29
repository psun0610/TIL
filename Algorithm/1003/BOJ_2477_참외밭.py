import sys
input = sys.stdin.readline

n = int(input())
list_ = [[] for i in range(5)]
seclist = []
for i in range(6):
    num, l = map(int, input().split())
    seclist.append(l)
    list_[num].append(l)
large, small, tmp = 1, 0, 0

print(list_)
print(seclist)
for i in range(1, 5):
    if len(list_[i]) == 1:
        large *= list_[i][0]
        tmp = seclist.index(list_[i][0])

small = seclist[(tmp + 2) % 6] * seclist[(tmp + 3) % 6]

print((large - small) * n)