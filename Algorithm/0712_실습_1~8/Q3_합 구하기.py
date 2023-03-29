# 3합 구하기
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지


# 방법 1
n = int(input())
sum, tmp = 0, 0
while tmp < n:
    tmp += 1
    sum += tmp
print (sum)

#방법 2
n = int(input())
sum, tmp = 0, 0
for tmp in range(n):
    tmp += 1
    sum += tmp
print(sum)