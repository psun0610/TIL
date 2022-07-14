# 14. 문자의 갯수 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
'''
word = input()
cnt = 0
for i in word:
    if i == 'a':
        cnt += 1
print (cnt)
'''

# 15. 문자의 위치 구하기
#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
'''
# 방법 1
word = input()
cnt = 0
for i in word:
    if i == 'a':
        break
    cnt += 1
else:
    cnt = -1
print(cnt)

# 방법 2 (강사님)
word = input()
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)

# 방법 3
word = input()
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break
if not is_a:
    print(-1)
'''

# 15 - 추가문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
'''
# 방법 1
word = input()
cnt = 0
for i in word:
    if i == 'a':
        print(cnt, end=' ')
    cnt += 1

# 방법 2 (강사님 - 리스트에 모아서 한 번에 출력하는  방법)
word = input()
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)
print(result)
'''

# 16. 모음 등장 여부
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지 확인하기
'''
# 방법 1
word = input()
cnt = 0
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
print(cnt)

# 방법 2 (강사님)
word = input()
count = 0
for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        count += 1
print(count)
'''

# 17. 소문자-대문자 변환하기
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
'''
word = input()
for i in word:
    print(chr(ord(i)-32), end='')
'''

# 18. 알파벳 등장 갯수 구하기
# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
'''
# 방법 1
word = input()
myDict = {}
for i in word:
    if char not in result:
    # if myDict.get(i) == None:
        myDict[i] = 1
    else:
        myDict[i] += 1

# 출력 방법 1
# for i in myDict:
#     print(i, myDict.get(i))

# 출력 방법 2
for k, v in myDict.items():
    print(k, v)

# 방법 2
result = {}
for char in word:
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1
print(result)

# 방법 3
result = {}
for char in word:
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

출력 방법
for key in result:
    print(key, result[key])
'''