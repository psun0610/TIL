# import sys
# input = sys.stdin.readline
# n = int(input())
# gomgom = []
# cnt = 0
# for _ in range(n):
#     status = input().strip()
#     if status == 'ENTER':
#         gomgom.clear()
#     elif status not in gomgom:
#         gomgom.append(status)
#         cnt += 1
# print(cnt)

import sys
input = sys.stdin.readline
n = int(input())
gomgom = {}
cnt = 0
for _ in range(n):
    status = input().strip()
    if status == 'ENTER':
        gomgom.clear()
        continue
    
    gomgom[status] = gomgom.get(status, 0) + 1

    if gomgom[status] == 1:
        cnt += 1

print(cnt)
