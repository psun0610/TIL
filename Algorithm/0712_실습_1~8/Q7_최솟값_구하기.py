# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [0, 20, 100]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)