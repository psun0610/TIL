# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

# 예시
# a, b = input().split()
# a=int(a)
# b=int(b)
# print(a)
# print(b)
# 과 같은 방법으로 두 정수를 입력받아 출력할 수 있다.

# 참고
# python의 input()은 한 줄 단위로 입력을 받는다.
# input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
# a, b = 1, 2
# 를 실행하면, a에는 1 b에는 2가 저장된다.
# (주의 : 하지만, 다른 일반적인 프로그래밍언어에서는 이러한 방법을 지원하지 않기 때문에 a=1, b=2 를 한 번에 하나씩 따로 실행시켜야 한다.)

a, b = map(int,input().split())
print(a)
print(b)