t = int(input())
for _ in range(t):
    alist = list(map(int, input().split()))
    for i in range(2):
        alist.pop(alist.index(max(alist)))
    print(alist.pop(alist.index(max(alist))))