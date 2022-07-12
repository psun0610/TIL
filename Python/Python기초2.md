# Python (2)

## 제어문

> 특정 상황에 따라 코드를 선택적으로 실행하거나 반복하는 제어
>
> 제어문은 순서도(flow chart)로 표현이 가능
>
> 조건문, 반복문으로 나뉨
>
> 파이썬은 **들여쓰기**로 구문을 구분하기 때문에 꼭 확인 잘 할 것

## 조건문

- ### if <조건식>: ~ else: ~

  ```python
  num = int(input())
  if num % 2 == 1:
      print('홀')
  else:
      print('짝')
  print(num)
  ```

- ### **복수 조건문**  if <조건식>: ~ elif <조건식>: ~

  ```python
  dust = 80
  
  if dust > 150:
      print('매우 나쁨')
  elif dust > 80:			# 150 >= dust > 80 으로 작성할 필요 없음
      print('나쁨')		   # 150 이상이라면 이미 위에서 '매우 나쁨'이 출력되고 조건문이 끝나기 때문
  elif dust > 30:
      print('보통')
  else:
      print('좋음')
  print('미세먼지 확인 완료')
  ```

- ### **중첩 조건문**  if <조건식>: ~ *if <조건식>:* ~ else: ~

  ```python
  dust = -10
  if dust > 150:
      print('매우 나쁨')
      if dust > 300:
          print('실외 활동을 자제하세요.')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      if dust >= 0:
          print('좋음')
      else:
          print('값이 잘못되었습니다.')
  ```

- ### **조건표현식**  <true인 경우 값> if <조건식> else <false인 경우 값>

  ```python
  value = num if num >= 0 else -num
  #     참일 경우   조건식      거짓일 경우
  # => 절댓값을 저장하기 위한 코드
  ```

  

## 반복문

- ### while 문

  - 조건식이 참인 경우 반복적으로 코드를 실행

  ```python
  a = 0
  while a < 4:	# 종료 조건
      print(a)
      a += 1
  print('끝')
  
  # 0
  # 1
  # 2
  # 3
  # 끝
  ```

  

- ### for 문

  - 순회 가능한 객체 요소를 **모두** 순회함 (시퀀스 포함), 종료조건 필요X

  ```python
  for fruit in ['apple', 'mango', 'banana']:
      print(fruit)
  print('끝')
  
  # apple
  # mango
  # banana
  # 끝
  ```

  - 문자열 순회

  ```python
  # 예시 1
  chars = input()
  # 입력: hi 라면
  for char in chars:
      print(char)
  # h
  # i
  
  # 예시 2
  chars = input()
  # 입력: hi 라면
  for idx in range(len(chars)):	#입력 문자열의 길이만큼 반복
      print(chars[idx])
  # h
  # i
  ```

  - enumerate 순회 ~~(많이 안 씀)~~: 인덱스와 객체를 쌍으로 담은 열거형 객체 '(index, value) tuple' 반환

  ```python
  members = ['민수', '영희', '철수']
  for i in range(len(members)):
      print(f'{i} {members[i]}')
  
  # 위 내용과 아래 내용 같음
  for i, member in enumerate(members):
      print(i, member)
      
  # 순회
  list(enumerate(members))
  #[(0, '민수'), (1, '영희'), (2, '철수')]
  list(enumerate(members, start=1))		# start의 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
  # [(1, '민수'), (2, '영희'), (3, '철수')]
  ```

  - 딕셔너리 순회: 키 값 반환(key값이 있으면 value를 찾을 수 있지만, value는 반환돼봤자 key를 찾지 못함)

  ```python
  grades = {'john': 80, 'eric': 90}
  for name in grades:
      print(name)
      
  # john
  # eric
  ```

    

- ### 반복 제어: break, continue, for-else

  - **break**: 반복문을 종료

  ```python
  # 예시 1
  n = 0
  while True:
      if n == 3:
          break
      print(n)     
      n += 1
      
  # 0
  # 1
  # 2
    
  # 예시 2
  for i in range(10):
  if i > 1:
  print('0과 1만 필요해!')
  break
  print(i)
  
  # 0
  # 1
  # 0과 1만 필요해!
  ```

    

  - **continue**: continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  ```python
  for i in range(6):
      if i % 2 == 0:
          continue
    	print(i)
      
  # 1
  # 3
  # 5
  ```

    

  - **for-else**: 끝까지 반복문을 실행한 이후에 else문 실행, **break를 통해 종료되는 경우 else문 실행 X**
  
  ``` python
  # 예시 1
  for char in 'apple':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # b가 없습니다.
  
  # 예시 2
  for char in 'banana':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # b!
  ```
  
  