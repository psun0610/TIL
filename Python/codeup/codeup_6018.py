# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

# 예시
# a, b = input().split(':')
# print(a, b, sep=':')
# 와 같은 방법으로 가능하다.

# 참고
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
# sep 는 분류기호(seperator)를 의미한다.
 
a, b = input().split(':')
print(a, b, sep=':')