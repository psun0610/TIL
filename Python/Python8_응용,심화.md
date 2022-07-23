# Python(8) 응용/ 심화
## List Comprehension
- `[<expression> for <변수> in <iterable>]
- `[<expression> for <변수> in <iterable> if <조건식>]`
> 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

ex) 1~3의 세제곱의 결과가 담긴 리스트 만들기
```python
cube_list = []
for number in range(1, 4):
    cubic_list.append(number**3)
print(cubic_list)
```
List Comprehension 사용
```python
[number**3 for number in range(1, 4)]
```
-> 특정한 원소(요소)로 구성된 리스트 만들 때 사용!

## Dictionary Comprehension
- `{key: value for <변수> in <iterable>}`
- `{key: value for <변수> in <iterable> if <조건식>}`
> 표현식과 제어문을 통해 특정한 키와 값을 가진 딕셔너리를 간결하게 생성하는 방법

ex) 1~3의 세제곱의 결과가 담긴 딕셔너리 만들기
```python
cubic_dict = {}
for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)
```
Dictionary Comprehension 사용
```python
{number: number**3 for number in range(1, 4)}
```
## lambda() 함수
- `lambda <parameter>: <표현식>`
> 표현식을 계산한 결과값을 반환하는 함수
> 이름이 없는 함수여서 익명함수라고도 불림
- 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
    - 함수를 정희해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용가능

ex 1) 람다함수 사용
```python
def plus_ten(x):
    return x + 10
print(plus_ten(1))
# 11
```
```python
plus_ten = lambda x: x + 10
print(plus_ten)
# 11
```
ex 2) `map()`함수와 같이 사용
```python
example = list(map(lambda x: x**2, range(5)))
print(example)
# [0, 1, 4, 9, 16]
```
ex 3) `reduce()`함수와 같이 사용
```python
from functools import reduce
print(reduce(lambda x, y: x + y, range(11))
# 55
```
```python
print(reduce(lambda x, y: y + x, 'abcde'))
# edcba
```
```python
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]

print(reduce(lambda acc, cur: acc + [cur['mail']], users, [])
```
## reduce() 함수
- `reduce(<function>, <iterable>, [초기값])`
- 집계 함수와 iterable은 필수, 초기값은 선택
> 반복 가능한 객체 내 각 요소를 함수로 연산한 뒤 이전 연산 결과들과 누적해서 반환해 주는 함수

## filter() 함수
- `filter(<function>, <iterable>)`
> 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환
```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
# <filter object at 0x10e4dcfc10> <class 'filter'>
print(list(result))    # 리스트 형변환을 통해 결과 직접 확인 가능
# [1, 3]
```

## 모듈
### 파이썬 표준 라이브러리
> 파이썬에 기본적으로 설치된 모듈과 내장 함수
- [파이썬 표준 라이브러리 — Python 3.10.5 문서](https://docs.python.org/ko/3/library/index.html)

### 파이썬 패키지 관리자(pip)
> PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

### 파이썬 패키지 관리자 명령어
- **패키지 설치**
    - `$ pip install SomePackage`
    - `$ install SomePackage==1.0.5`
    - `$ pip install 'SomePackage>=1.0.4'`
    - 최신/ 특정/ 최소 버전을 명시하여 설치 할 수 있음
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
    - **bash, cmd 환경에서 사용되는 명령어**
    - 
- **패키지 삭제**
    - `$ pip uninstall SomePackage`
    - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

- **패키지 목록 및 특정 패키지 정보**
    - `$ pip list`
    - `$ pip show SomePackage`

- 패키지 활용 명령어
    - **패키지 freeze**
        - `pip freeze`
        - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
        - 해당하는 목록을 *requirements.txt(관습)*으로 만들어 관리함
    - **패키지 관리하기**
        - `$ pip freeze > requirements.txt`
        - `$ pip install -r requirements.txt`
        - 위 명령어들을 통해 패키지 목록을 관리(1)하고 설치(2)할 수 있음
        - 일반적으로 패키지를 기록하는 파일의 이름은 *requirements.txt*로 정의함

## 가상 환경
- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 과거 외주 프로젝트 - django 버전 2.x
    - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음
- 프로젝트별 가상환경을 따로 만들면 폴더별로 고유한 프로젝트가 설치됨

### venv
- 가상 환경을 만들고 관리하는 데 사용되는 모듈
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    - 특정 폴더에 가상환경(패키지 집합 폴더 등)이 있고
    - 실행 환경(ex. bash)에서 가상 환경을 활성화 시켜
    - 해당 폴더에 있는 패키지를 관리/ 사용함

### 가상 환경 생성
- `$ python -m venv <폴더명>`
- 가상 환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

### 가상 환경 활용
- 아래의 명령어를 통해 가상 환경을 활성화
    - `<venv>`는 가상환경을 포함하는 디렉토리의 이름
    - 가상 환경 비활성화는 `$ deactivate` 명령어를 사용

| 플랫폼   | 셀               | 가상 환경을 활성화하는 명령                       |
|:-----:|:---------------:|:-------------------------------------:|
| POSIX | bash/zsh        | `$ source <venv> /bin/activate`       |
|       | fish            | `$ source <venv> /bin/activate.fish`  |
|       | csh/tchs        | ` $ source <venv> /bin/activate.csh`  |
|       | PowerShell Core | `$ <venv> /bin/Activate.ps1`          |
| 윈도우   | cmd.exe         | `C:\> <venv> \Scripts\activate.bat`   |
|       | PoserShell      |                                       |
