import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 'Yes'
for i in range(m):
    k = int(input())                    # i번째 더미에 쌓인 책의 개수
    book_stack = list(map(int, input().split()))    # i번째 더미에 쌓인 책 (아래부터 번호대로 주어짐), 스택으로 활용할 것
    prev = book_stack.pop()
    for j in range(k - 1):
        current = book_stack.pop()
        if prev > current:
            ans = 'No'
        else:
            prev = current
print(ans)