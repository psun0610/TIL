import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 'Yes'
for i in range(m):
    k = int(input())
    books = list(map(int, input().split()))
    if sorted(books, reverse=True) != books:
        ans = 'No'
print(ans)