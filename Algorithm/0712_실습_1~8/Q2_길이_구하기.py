# 2. 길이 구하기
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

word = input()
length = 0
while(length < len(word)):
    length += 1
print(length)