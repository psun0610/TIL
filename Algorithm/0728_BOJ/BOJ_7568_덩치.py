n = int(input())
list_ = []
ranks = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    list_.append((x, y))

for a in range(n):
    # A는 기준이 되는 사람
    A = list_[a]
    for b in range(n):
        # 비교가 되는 사람
        B = list_[b]

        # B가 A보다 덩치가 작다.
        if A[0] > B[0] and A[1] > B[1]:
            # B보다 덩치가 큰 사람이 한명 더 있다. +1
            ranks[b] += 1
for rank in ranks:
    print(rank + 1, end=' ')