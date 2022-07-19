# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

number = int(input())
total = 0
while number:
    total += (number % 10)
    number //= 10
print(total)