import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    words = list(input().strip().split(' '))
    ans = []
    for word in words:
        ans.append(word[::-1])
    print(*ans)