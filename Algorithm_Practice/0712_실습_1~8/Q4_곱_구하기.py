# 4. 곱 구하기
# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# 방법 1
n = int(input())
mul, tmp = 1, 0
while tmp < n:
    tmp += 1
    mul *= tmp
print (mul)


# 방법 2
n = int(input())
mul, tmp = 1, 0
for tmp in range(n):
    tmp += 1
    mul *= tmp
print(mul)