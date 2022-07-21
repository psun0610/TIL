# Python(5) 에러/ 예외 처리
에러가 가장 많이 발생하는 구간으로, 중점적으로 봐야할 부분은 **제어가 되는 시점**이다.
즉 조건/ 반복문과 함수에서 가장 많이 발생한다.

## 디버깅
- **중점적으로 봐야할 부분**
    - branches: 모든 조건이 원하는대로 동작하는지
    - for loops: 반복문에 진입을 하는지, 원하는 횟수만큼 실행되는지
    - while loops: for loops와 동일, 종료조건이 제대로 동작하는지
    - function: 함수 호출시, 함수 파라미터, 함수 결과
- **디버깅 하는 방법**
    - print 함수 활용: 특정 함수의 결과, 반복/ 조건 결과 등을 나눠서 생각
    - 개발 환경에서 제공하는 기능 활용: breakpoint, 변수 조회 등
    - Python tutor 활용: 단순 파이썬 코드인 경우
    - 뇌컴파일, 눈디버깅

## 에러와 예외
### 문법 에러
> 프로그램이 실행되지 않음
> 파일이름, 줄번호, ^문자를 통해 문제가 발생한 위치를 표현해줌
> 줄에서 에러가 감지된 가장 앞의 위치를 캐럿(^)기호로 표시

- **EOL (End Of Line)**: 문자열을 닫지 않은 경우, 다른 종류의 따옴표로 문자열을 만든 경우 발생
```python
print('hello
# File "<ipython-input-6-2a5f5c6b1414>", line 1
# print('hello
# ^
# SyntaxError: EOL while scanning string literal
      
print('hello")
# File "&lt;stdin&gt;", line 1
#       'a"
#        ^ 
# SyntaxError: EOL while scanning string literal
```
- **EOF (End Of File)**: 갑자기 파일이 끝난 경우 발생
 ```python
print(
# File "<ipython-input-4-424fbb3a34c5>", line 1
# print(
# ^
# SyntaxError: unexpected EOF while parsin
```
- **Invalid syntax**: 파이썬 문법에 맞지 않는 경우
```python
while
# File "<ipython-input-7-ae84bbebe3ce>", line 1
# while
# ^
# SyntaxError: invalid syntax
```
-**assign to literal**: 식별자가 아닌 리터럴에 값을 할당한 경우
```python
5 = 3
# File "<ipython-input-28-9a762f2c796b>", line 
1
# 5 = 3
# ^
# SyntaxError: cannot assign to literal
```

### 예외
> 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러, 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤
> 프로그램 실행 중에 감지되는 에러를 예외라고 부름
> 모든 내장 예외는 Exception Class를 상속받아 이루어짐
> 사용자 정의 예외를 만들어 관리할 수 있음

- **ZeroDivisionError**: 0으로 나누고자 할 때 발생
```python
10/0
# ---------------
# ZeroDivisionError Traceback (most recent call last)
# ----> 1 10/0
# ZeroDivisionError: division by zero
```
- **NameError**: namespace 상에 이름이 없는 경우 발생
```python
print(name_error)
# ---------------------------
# NameError Traceback (most recent call last)
# ----> 1 print(name_error)
# NameError: name 'name_error' is not define
```
- **TypeError**: 타입 불일치
```python
1 + '1'
# --------------
# TypeError Traceback (most recent call last)
# ----> 1 1 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
```python
round('3.5')
# ---------------
# TypeError Traceback (most recent call last)
# ----> 1 round('3.5')
# TypeError: type str doesn't define __round__ method
```
- **TypeError**: arguments 부족
```python
divmod()
# ------------
# TypeError Traceback (most recent call last)
# ----> 1 divmod()
# TypeError: divmod expected 2 arguments, got 0
```
```python
import random random.sample()
# ---------
# TypeError Traceback (most recent call last)
# 1 import random
# ----> 2 random.sample()
# TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
```
- **TypeError**: argument 개수 조과
```python
divmod(1, 2, 3)
# ---------
# TypeError Traceback (most recent call last)
# ----> 1 divmod(1, 2, 3)
# TypeError: divmod expected 2 arguments, got 3
```
```python
import random
random.sample(range(3), 1, 2)
# --------
# TypeError Traceback (most recent call last)
# 1 import random
# ----> 2 random.sample(range(3), 1, 2)
# TypeError: sample() takes 3 positional arguments but 4 were given
```
- **ValueError**: 타입은 올바르나 값이 적절하지 않거나 없는 경우
```python
int('3.5')
# ------
# ValueError Traceback (most recent call last)
# ----> 1 int('3.5')
# ValueError: invalid literal for int() with base 10: 
'3.5'
```
```python
range(3).index(6)
# ------
# ValueError Traceback (most recent call last)
# ----> 1 range(3).index(6)
# ValueError: 6 is not in range
```
- IndexError: 해당하는 인덱스가 없는데 호출한 경우
```python
empty_list = []
empty_list[2]
# ------
# IndexError Traceback (most recent call last)
# 1 empty\_list = \[\]
# ----> 2 empty\_list\[2\]
# IndexError: list index out of range
```
- **KeyError**: 해당하는 키가 없는데 호출한 경우
```python
song = {'IU': '좋은날'}
song['BTS']
# ------ 
# KeyError Traceback (most recent call last) 
# 1 song = {'IU': '좋은날'} 
# ----> 2 song\['BTS'\] 
# KeyError: 'BTS'
```
- **ModuleNotFoundError**: 존재하지 않는 모듈을 import 하는 경우
```python
import nonamed
# ------ 
# ModuleNotFoundError Traceback (most recent call last) 
# ----> 1 import nonamed 
# ModuleNotFoundError: No module named 'nonamed'
```
- **ImportError**: 모듈은 있으나 존재하지 않는 클래스/ 함수를 가져오는 경우
```python
from random import samp
# ------ 
# ImportError Traceback (most recent call last) 
# ----> 1 from random import samp 
# ImportError: cannot import name 'samp' from 'random'
```
- **IndentationError**: 들여쓰기(Indentation)가 적절하지 않는 경우
```python
for i in range(3):
    print(i)
# File "", line 2
# print(i) 
# ^ 
# IndentationError: expected an indented block
```
- **KeyboardInterrupt**: `ctrl+c`등으로, 임의로 프로그램을 종료했을 때
```python
while True:
continue
# ------
# KeyboardInterrupt Traceback (most recent call last)
# <ipython-input-55-6a65cf439648> in <module>
# 1 while True:
# ----> 2 continue
# KeyboardInterrupt:
```

## 예외처리
> `try 문 (statement)/ exept 절 (clause)`을 이용하여 예외 처리를 할 수 있음

### Try, Except, Else, Finally
- try 문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생하지 않으면, except 없이 실행 종료
- except 문
    - try 문에서 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- else 문
    - try 문에서 예외가 발생하지 않으면 else문이 실행
- finally 문
    - 예외 발생 여부와 관계없이 항상 실행

### 작성 방법
```python
try:
    try 명령문
except 예외그룹-1 as 변수-1:
    예외처리 명령문 1
except 예외그룹-2 as 변수-2:
    예외처리 명령문 2
finally: #선택사항
    finally 명령문
```
**try문은 반드시 한 개 이상의 except문이 필요!!**

- 예시 1
```python
try:
    num = input('숫자입력 :')
    print(int(num))
except ValueError:
    print('숫자가 아닙니다')
```
- 예시 2-1   **발생 가능한 에러를 모두 명시**
```python
try:
num = input('100으로 나눌 값을 입력하시오: ')
100/int(num)
except (ValueError, ZeroDivisionError):
print('제대로 입력해줘')
```
- 예시 2-2   **에러 별로 별도의 에러 처리**
```python
try:
num = input('값을 입력하시오: ')
100/int(num)
except ValueError:
print('숫자를 넣어주세요.')
except ZeroDivisionError:
print('0으로 나눌 수 없습니다.')
except:
print('에러는 모르지만 에러가 발생하였습니다.')
```
- 예시 3   파일을 열고 읽는 코드 작성
```python
try: 
    f = open('nooofile.txt')
except FileNotFoundError:
    print('해당 파일이 없습니다.')
else:
    print('파일을 읽기 시작합니다.')
    print(f.read())
    print('파일을 모두 읽었습니다.')
    f.close()
finally:
    print('파일 읽기를 종료합니다.')
```
## 예외 발생 시키기
> 의도적으로 raise를 사용하여 예외를 발생시킬 수 있음
> 대체 왜 쓰는가???
> 바로 소프트웨어를 만들어서 개발자들이 사용하도록 할 때 의도하지 않게 돌아가는 것을 방지하기 위해서 일부러 에러를 발생 시킴
### raise statement
`raise <표현식> (메시지)`를 통해 예외를 강제로 발생시킬 수 있음
표현식에는 예외 타입을 지정하고, 주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴
- 예시 1  그냥 raise
```python
raise
# -------
# RuntimeError Traceback (most recent call last)
# ----> 1 raise
# RuntimeError: No active exception to reraise
```
- 예시 2   raise 적용
```python
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생
if a < 1 or a > 5:
    raise

# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")
```
- 예시 3   **raise + 예외 처리 이름(파이썬 내장 예외)**
```python
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생
if a < 1 or a > 5:
    raise ValueError
    
# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")

# 1~5 까지 숫자 입력 : 6
# Traceback (most recent call last):
#   File "c:\Users\TFX255GS\Desktop\TIL\Python\Test.py", line 5, in <module>
#     raise ValueError
# ValueError
```
- 예시 4   **raise + 메시지**
```python
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생
if a < 1 or a > 5:
    raise Exception("에러!!")

# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")

# 1~5 까지 숫자 입력 : 6
# Traceback (most recent call last):
#   File "c:\Users\TFX255GS\Desktop\TIL\Python\Test.py", line 5, in <module>
#     raise Exception("에러!!")
# Exception: 에러!!
```
- 예시 5   **try + raise + except**
    - 이렇게 처리하면 에러가 발생했을 때 프로그램이 비정상 종료되는 것이 아니라, except 구문이 실행되며 예외처리가 된다!
```python
try:
    a = int(input("1~5 까지 숫자 입력 : "))

    # 범위를 벗어나면 error 발생!
    if a < 1 or a > 5:
        raise

    # 범위 안에 있으면 정상 출력
    print(f"입력한 a : {a} 입니다.")
except:
    print("1~5 사이만 입력하세요")

# 1~5 까지 숫자 입력 : 0
# 1~5 사이만 입력하세요