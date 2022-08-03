# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

# 예시
# a = bool(int(input()))
# print(not a)

# 참고
# a = bool(int(input()))
# 와 같은 형태로 겹쳐 작성하면, 한 번에 한 단계씩 계산/처리/평가된다.
# 위와 같은 명령문의 경우 input( ), int( ), bool( ) 순서로 한 번에 한 단계씩 계산/처리/평가된다.

# 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능하다.

# 참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용할 수 있다.

# 이러한 논리연산을 NOT 연산(boolean NOT)이라고도 부르고,
# 프라임 '(문자 오른쪽 위에 작은 따옴표), 바(기호 위에 가로 막대), 문자 오른쪽 위에 c(여집합, complement) 등으로 표시한다.
# 모두 같은 의미이다.

# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
# 불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산 된다.

# 정수값 0은 False 이고, 나머지 정수 값들은 True 로 평가된다.
# 빈 문자열 "" 나 ''는 False 이고, 나머지 문자열들은 True 로 평가된다.

num = bool(int(input()))
print(not num)
