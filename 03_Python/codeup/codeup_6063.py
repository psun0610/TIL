# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# 예시
# a, b = input().split()
# a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
# b = int(b)
# c = (a if (a>=b) else b)
# print(int(c))

# 참고
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값

# 조건식 또는 값이 True 이면 x 값이 사용되고, True가 아니면 y 값이 사용되도록 하는 코드이다.

# 예를 들어
# 0 if 123>456 else 1
# 과 같은 표현식의 평가값은 123 > 456 의 비교연산 결과가 False 이므로 1이 된다.

# 예시 코드에서
# a>=b 의 결과가 True(참) 이면 (a if (a>=b) else b)의 결과는 a가 되고,
# a>=b 의 결과가 False(거짓)이면 (a if (a>=b) else b)의 결과는 b가 된다.

a, b = map(int, input().split())
print(int(a if (a>=b) else b))