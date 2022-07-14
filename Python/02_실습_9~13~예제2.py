# 9. 득표수 구하기
# 영희 득표수 출력
'''
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt = 0
for i in students:
    if i == '이영희':
        cnt += 1

print(cnt)
'''

# 10. 5의 개수 구하기
'''
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0
for i in numbers:
    if i == 5:
        cnt += 1
print(cnt)
'''

# 11. 구구단 출력하기
# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
'''
dan = 1
while(dan < 9):
    dan += 1
    print(f'{dan}단')
    num = 0
    while(num < 9):
        num += 1
        print(f'{dan} X {num} = {dan*num}')
'''

# 12. 문자열 조작하기
# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
'''
word = input()
new_word = ''
for i in word:
    if i != 'a':
        new_word += i
print (new_word)
'''

# 13-1. 문자열 조작하기2
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
'''
word = input()
print(word[::-1])
'''

# 13-2
# 문자열 인덱스 이용하여 풀이 ***중요***
word = input()
cnt = 0
for char in word:
    print(word[len(word)-cnt-1], end='')
    cnt += 1


# 예제 1. 기초 함수
# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오
'''
def cube(n):
    return n ** 3
print(cube(12))
'''

# 예제 2. 기초 함수2
# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로 
# * 사각형 둘레 : (가로 + 세로) * 2
'''
def rectangle(a, b):
    return a * b, (a+b) * 2
print(rectangle(20, 30))
'''