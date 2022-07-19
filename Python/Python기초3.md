# Python(3) 파이썬의 함수
## 함수
> 특정한 기능을 하는 코드의 묶음
> 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에 호출하여 간편히 사용

- 함수를 사용하는 이유
  - 코드 중복 방지
  - 재사용 용이

- 함수의 기본 구조
  - 선언과 호출(define & call)
  - 입력(Input)
  - 범위(Scope)
  - 결과값(Output)
  ```python
  def <함수이름>(인자 parameters):  # parameters = INPUT
    <Docstring> #Documentation String
    <function body>   # function body = SCOPE
    return <리턴 값>  # return = OUTPUT
  ```

- 선언과 호출
  - 선언
    - 선언은 def 키워드 활용
    - 들여쓰기를 통해 코드 블럭 구분
      - Docstring은 함수 body 앞에 선택적으로 작성함(작성시에는 반드시 첫 번째 문장에 문자열 ''' ''')
    - 함수는 인자(parameter)를 넘겨줄 수 있음
    - 동작 후에 `return`을 통해 결과값을 전달함
  - 호출
    - `함수명(값)`으로 호출
    - 함수는 호출되면 코드를 실행하고 return 값을 반환하며 종료됨
    ```python
    num1 = 0
    num2 = 1

    def func1():
        return 0
    def func2(a):
        return a+1
    def func3(a, b):
        return a+b
    def func4(a, b):
        return func2(a) + func3(5, b)

    result1 = func1()
    result2 = func2(num1)
    result3 = func3(num1, num2)
    result4 = func4(num1, num2)
    print(result1, result2, result3, result4)
    # 0 1 1 7
    ```

## 함수의 결과값(Output)
- return
  - 함수는 반드시 하나의 값을 return
  - 만약 명시적인 return이 없을 경우에는 None을 반환
  - 함수는 return과 동시에 실행이 종료됨
  - return문을 한번만 사용하면서 두 개 이상의 값을 반환하려면 **튜플**을 이용함
  ```python
  def minus_and_product(x, y):
    return x-y, x*y
  
  minus_and_product(4,5)
  # (-1, 20) 튜플 반환됨
  ```

## 함수의 입력(Input)
- parameter VS argument
  - parameter: 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  - argument: 함수를 호출 할 때, 넣어주는 값
  ```python
  def function(ham): # parameter : ham
    return ham
  function('spam') # argument: 'spam'
  ```

### Argument란?
- 함수 호출 시 함수의 Parameter를 통해 전달되는 값
- 소괄호 안에 할당 function_name(**argument**)
- 필수 Argument와 선택 Argument로 나뉨
  - 필수 Argument: 반드시 전달되어야 하는 argument
  - 선택 Argument: 값을 전달하지 않아도 되는 경우에 기본 값 전달 (Parameter에 이미 기본 값이 설정되어 있는 경우)
- Positional Arguments
  - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수에 전달됨
- Keyword Arguments
  - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
  - **Keyword Argument 다음에 Positional Argument를 활용할 수 없음** (이미 위치가 흐트러졌기 때문에)
   ```python
    def add(x, y):
      return x+y
    
    add(x=2, y=5)
    add(y=5, x=2)
    add(2, y=5)
    add(y=5, 2) # 에러발생! Keyword Argument 다음에 Positional Argument가 위치했기 때문
   ```
- Default Arguments Values
  - 기본값을 지정하여 Argument 값을 설정하지 않아도 되게 함
  - 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음
   ```python
    def add(x, y=0):
      return x+y

    add(2)
    # 2
   ```
- **정해지지 않은 개수의 Arguments**
  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  - Argument들은 **튜플**로 묶여서 처리됨
  - parameter의 앞에 *를 붙여 표현
   ```python
    def add(*args):
      for arg in args:
        print(arg)
    
    add(2)
    add(2, 3, 4, 5)
   ```
- **정해지지 않은 개수의 Keyword Arguments**
  - 여러 개의 KeyWord Argument를 하나의 필수 parameter로 받아서 사용
  - Argument들은 **딕셔너리**로 묶여 처리
  - parameter의 앞에 **를 붙여 표현
   ```python
    def family(**kwargs):
      for key, value in kwargs:
        print(key, ':', value)

    family(father='John', mother='Jane', me='John Jr.')
   ```
  
## 함수의 범위(Scope)
> 함수는 코드 내부에 local scope를 생성함
> 그 외의 공간은 global scope로 구분

### scope
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
  - global variable: global scope에 정의된 변수
  - local variable: local scope에 정의된 변수

### 객체 생명 주기
  - built-in scope: 파이썬이 실행된 이후부터 영원히 유지
  - global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope: 함수가 호출될 때 생성, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)
  - 파이썬에서 사용되는 이름(식별자)들은 namespace에 저장되어 있음
  - **LEGB Rule**
    - **L**ocal scope: 함수
    - **E**nclosed scope: 특정 함수의 상위 함수
    - **G**lobal scope: 함수 밖의 변수, Import 모듈
    - **B**uilt-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성
  - 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
  ```python
  print(sum)
  # <built-in function sum>
  print(sum(range(2)))
  # 1
  sum = 5
  print(sum)
  # 5
  print(sum(range(2))
  # 에러발생! TypeError: 'Int' object is not callable
  ```

## 함수 응용
- 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(Type)이 내장되어 있음
- map
  - 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function)을 적용하고, 그 결과를 map object로 반환
  ```python
  numbers = [1, 2, 3]
  result = map(str, numbers)
  print(result, type(result))
  # <map object at 0x10e2ca100> <class 'map'>
  
  list(result)  # 리스트 형변환을 통해 결과를 직접 확인할 수 있다.
  # ['1', '2', '3']
  ```
  - input 값들을 숫자로 바로 활용하고 싶을 때
  ```python
  n, m = map(int, input().split())
  ```
  [!python_map](Python기초3.assets/map.jpg)
  1. input()
    - 사용자에게 입력을 받는 함수
    - 타입: 항상 string
  2. 문자열.split()
    - 구분값을 기준으로 쪼개서 리스트에 넣어주는 함수
    - 타입: 항상 list
  3. input().split()
    - 문자열로 받은 것을 각각 공백을 기준으로 리스트로 쪼갬
    - 결과: ['10', '20]
  4. map(함수, 반복 가능한 타입의 것)
    - 어떤 함수를 반복 가능한 것들의 요소에 모두 적용시킴
  5. map(int, input().split())
    - int() 함수를 input().split() 리스트의 모든 요소에 적용함
    - 결과: map object [10, 20]
  6. print(n*m)
    - n, m = [10, 20]
    - 결과: 200