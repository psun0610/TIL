import sys

input = sys.stdin.readline

n, k = map(int, input().split())
list_ = [i for i in range(1, n + 1)]
current = 0
result = []

for i in range(n):
    # 현재 몇번째를 지울지 정함
    current += k - 1
    if current >= len(list_):
        # 만약에 범위를 넘으면 다시 처음부터 돌아가야하니까 나머지 계산
        current = current % len(list_)
    # 현재 지울 거 지우고 결과 리스트에 append
    result.append(list_.pop(current))

answer = ""
for i in range(len(result)):
    if i + 1 != len(result):
        answer += str(result[i]) + ", "
    else:
        answer += str(result[i])
print("<" + answer + ">")
