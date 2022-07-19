# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

# 방법 1
number = int(input())
total = 0
while number:
    total += (number % 10)
    number //= 10
print(total)

# 방법 2
# dimod(x, y)는 x를 y로 나누고, 결과를 tuple로 반환 => (몫, 나머지)
number = int(input())
total = 0
while number:
    total, remainder = divmod(number, 10)
    total += remainder
print(total)
