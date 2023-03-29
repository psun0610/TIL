n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))
ordered = {}
for i in range(len(sorted_numbers)):
    ordered[sorted_numbers[i]] = i

for number in numbers:
    print(ordered.get(number), end=' ')


# 출력부만 다름
n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))
ordered = {}
for i in range(len(sorted_numbers)):
    ordered[sorted_numbers[i]] = i
answer = []

for number in numbers:
    answer.append(ordered.get(number))

print(*answer)