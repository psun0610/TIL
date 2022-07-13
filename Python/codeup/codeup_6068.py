# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# 예시
# ...
# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D') 
# ...

# 참고
# 여러 조건들을 순서대로 비교하면서 처리하기 위해서 조건문을 여러 번 중첩할 수 있다.

score = int(input())
if score >= 90:
  print('A')
elif score >=70:
    print('B')
elif score >= 40:
    print('C')
else :
    print('D') 