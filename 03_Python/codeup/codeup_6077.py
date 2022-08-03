# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 예시
# #다음 코드는 홀 수만 더해 출력한다.
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#   if i%2==1 :
#     s += i

# print(s)

# 참고
# while 이나 for 반복실행구조를 이용할 수 있다.
# 다른 방법이나 while 반복실행구조를 이용해서도 성공시켜 보자.

num = int(input())
total = 0
for i in range(0, num+1, 2):
    total += i
print(total)