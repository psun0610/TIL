# 1. 수 구분하기
# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
'''
n = int(input())
if n%3 == 0 and n%2 == 0:
	 print('참')
else:
	 print('거짓')
'''

# 2. 길이 구하기
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.
'''
word = input()
length = 0
while(length < len(word)):
    length += 1
print(length)
'''

# 3-1. 합 구하기
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지
'''
n = int(input())
sum, tmp = 0, 0
while tmp < n:
    tmp += 1
    sum += tmp
print (sum)
'''

# 3-2
'''
n = int(input())
sum, tmp = 0, 0
for tmp in range(n):
    tmp += 1
    sum += tmp
print(sum)
'''

# 4-1. 곱 구하기
# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
'''
n = int(input())
mul, tmp = 1, 0
while tmp < n:
    tmp += 1
    mul *= tmp
print (mul)
'''

# 4-2
'''
n = int(input())
mul, tmp = 1, 0
for tmp in range(n):
    tmp += 1
    mul *= tmp
print(mul)
'''

# 5. 평균 구하기
# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

'''
numbers = [3, 10, 20]
sum, length = 0, 0
for i in numbers:
    length += 1
    sum += i
print(sum/length)
'''

# 6. 최댓값 구하기
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지
'''
numbers = [-10, -100, -30]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
'''

# 7. 최솟값 구하기
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

'''
numbers = [0, 20, 100]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)
'''

# 8-1. 두번째로 큰 수 구하기
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지
'''
numbers = [-10, -100, -30]
numbers = list(set(numbers))

max = numbers[0]
for i in numbers:
    if i > max:
        max = i
numbers.remove(max)

second_max = numbers[0]
for i in numbers:
    if i > second_max:
        second_max = i
print(second_max)
'''

# 8-2
'''
numbers = [0, 20, 100, 50, -60, 50, 100] # 50
numbers = list(set(numbers))
numbers.sort()
print(numbers[-2])
'''

# 8-3
numbers = [-10, -100, -30] # -30
numbers = list(set(numbers))
max, sec_max = numbers[0], numbers[0]
for i in numbers:
	if max < i:
		max = i
	elif sec_max < i < max:
		sec_max = i
print(sec_max)