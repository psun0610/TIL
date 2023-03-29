# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# 방법 1
number = int(input())
result = []
while number:
    result.append(number%10)
    number //= 10
for i in result:
    print(i, end='')


# 방법 2
number = int(input())
result = 0
while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 결과에 나머지를 더하고
    result += number%10
    # number를 10을 나눈 몫 넣음
    number //= 10

print(result)