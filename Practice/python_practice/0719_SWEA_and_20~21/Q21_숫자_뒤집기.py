# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

number = int(input())
result = []
while number:
    result.append(number%10)
    number //= 10
for i in result:
    print(i, end='')