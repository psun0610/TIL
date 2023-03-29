# mode 사용하여 최빈값 구하기
from statistics import mode
numbers = []
for _ in range(10):
    numbers.append(int(input()))

print(int(sum(numbers)/10))
print(mode(numbers))

# mode 사용 X
numbers = []
for _ in range(10):
    numbers.append(int(input()))

print(int(sum(numbers)/10))

list_ = list(set(numbers))
cnt = []

for i in range(len(list_)):
    cnt.append(numbers.count(list_[i]))

print(list_[cnt.index(max(cnt))])