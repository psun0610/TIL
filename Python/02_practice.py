#1
'''
n = int(input())
if n%3 == 0 and n%2 == 0:
	 print('참')
else:
	 print('거짓')
'''

#2
'''
word = input()
length = 0
while(length < len(word)):
    length += 1
print(length)
'''

#3-1
'''
n = int(input())
sum, tmp = 0, 0
while tmp < n:
    tmp += 1
    sum += tmp
print (sum)
'''

#3-2
'''
n = int(input())
sum, tmp = 0, 0
for tmp in range(n):
    tmp += 1
    sum += tmp
print(sum)
'''

# 4-1
'''
n = int(input())
mul, tmp = 1, 0
while tmp < n:
    tmp += 1
    mul *= tmp
print (mul)
'''

'''
# 4-2
n = int(input())
mul, tmp = 1, 0
for tmp in range(n):
    tmp += 1
    mul *= tmp
print(mul)
'''

#5
'''
numbers = [3, 10, 20]
sum, length = 0, 0
for i in numbers:
    length += 1
    sum += i
print(sum/length)
'''

#6
'''
numbers = [-10, -100, -30]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
'''

#7
'''
numbers = [0, 20, 100]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)
'''

#8-1
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

#8-2
'''
numbers = [0, 20, 100, 50, -60, 50, 100] # 50
numbers = list(set(numbers))
numbers.sort()
print(numbers[-2])
'''

#8-3
numbers = [-10, -100, -30] # -30
numbers = list(set(numbers))
max, sec_max = numbers[0], numbers[0]
for i in numbers:
	if max < i:
		max = i
	elif sec_max < i < max:
		sec_max = i
print(sec_max)