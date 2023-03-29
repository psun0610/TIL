n = int(input())
list_ = [0] * 5
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        list_[4] += 1
    elif x > 0 and y > 0:
        list_[0] += 1
    elif x < 0 and y > 0:
        list_[1] += 1
    elif x < 0 and y < 0:
        list_[2] += 1
    elif x > 0 and y < 0:
        list_[3] += 1
for i in range(4):
    print(f'Q{i + 1}: {list_[i]}')
print(f'AXIS: {list_[4]}')