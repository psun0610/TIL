# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = a - b
# print(c)

# 참고
# 수 - 수는 차(subtraction)가 계산된다.

a, b = input().split()
result = int(a)-int(b)
print(result)