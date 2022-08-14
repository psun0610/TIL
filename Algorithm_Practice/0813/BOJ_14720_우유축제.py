n = int(input())
milks = list(map(int, input().split()))
answer = 0
cur = 0
for milk in milks:
    if milk == cur % 3:
        answer += 1
        cur += 1
print(answer)
        