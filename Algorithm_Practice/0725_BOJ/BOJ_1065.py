N = int(input())
count = 0
for i in range(1, N + 1):
    num = list(map(int, str(i)))
    if i < 100:
        count += 1
    else:
        if num[0] - num[1] == num[1] - num[2]:
            count += 1
print(count)