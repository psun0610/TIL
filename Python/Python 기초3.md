# Python (3)
## 함수
> 특정한 기능을 하는 코드의 묶음
> 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에 호출하여 간편히 사용

-함수를 사용하는 이유
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
## 함수의 입력(Input)
## 함수의 범위(Scope)
## 함수 응용