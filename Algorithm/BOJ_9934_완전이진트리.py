import sys
input = sys.stdin.readline

k = int(input())
list_ = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def pre_order(list_, n, h):
    if n == 1:
        tree[h].append(list_[0])
        return
    tree[h].append(list_[n//2])
    h += 1
    pre_order(list_[:n//2], n//2, h)
    pre_order(list_[n//2+1:], n//2, h)

n = 2**k-1
pre_order(list_, n, 0)

for t in tree:
    print(*t)