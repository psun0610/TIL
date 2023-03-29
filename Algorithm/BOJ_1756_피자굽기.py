import sys

input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

bottom = d
for pizza in pizzas:
    tmp = 0
    for oven_depth in range(len(oven)):
        # 1. bottom(지금까지 쌓은 피자 위치)보다 오븐 깊이가 작아야 더 내려갈 수 있음
        # 2. 다음 oven이 피자 지름보다 크거나 같으면 한 칸 더 내려갈 수 있음
        if bottom > oven_depth + 1 and oven[oven_depth] >= pizza:
            tmp += 1
        else:
            bottom = tmp
            break
if bottom <= 0:
    print(0)
else:
    print(bottom)
