import sys

input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
tmp_list = []
for line in lines:
    for tmp in tmp_list:
        if tmp[0] >= line[0] and tmp[1] <= line[1]:
            tmp[1] = line[1]
            break

line_length = 0
for tmp in tmp_list:
    line_length += tmp[1] - tmp[0]

print(line_length)
