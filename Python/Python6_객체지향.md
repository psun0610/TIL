# Python(6) 객체지향 프로그래밍
> 파이썬은 모두 객체로 이루어져있음
> 이때 객체는 특정 **타입**의 **인스턴스**
- 123, 900, 5 는 모두 int의 인스턴스
- 'hello', 'bye'는 모두 string의 인스턴스
- [123, 56, 7], []는 모두 list의 인스턴스

## 객체
> 특정 타입의 인스턴스
- 객체의 특징
    - 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute): 어떤 상태(데이터)를 가지는가?
    - 조작법(method): 어떤 행위(함수)를 할 수 있는가?

## 객체지향 프로그래밍이란?
> 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- 절차지향 프로그래밍: 절차를 중심으로 데이터와 함수의 변화를 프로그래밍함
- 객체지향 프로그래밍: 데이터와 기능(메서드)로 분리, 추상화된 객체들간의 상호작용을 프로그래밍함

## 객체지향 프로그래밍의 특징
### 추상화
> 데이터나 기능을 의미나 수행과정이 비슷한 개념으로 묶어 정의(선언)하는 것

### 캡슐화
> 변수와 메소드가 하나의 캡슐 안에 묶인 특성
> 속성과 행위를 목적에 적합하게 묶어서 독립된 단위로 구성하는 것
> 파이썬은 캡슐화는 지원(class)하지만 내부 데이터들은 public으로 제공함(protected, private으로 변경 가능)
> 캡슐 안의 정보들은 밖에서 접근이 불가능하여 정보은닉이 가능함
> 결합도는 낮을수록, 응집도는 높을수록 좋음!
> 결합도: 메소드가 다른 메소드에 의존하는 정도
> 응집도: 메소드 내부 요소들의 관련 정도

### 상속성
> 기존의 클래스를 상속받아 새로운 기능을 추가한 새로운  클래스를 만들 수 있음
> 이때 기존 클래스는 부모클래스(슈퍼클래스), 상속받은 클래스는 자식클래스(서브클래스)

### 다형성
> 하나의 객체가 여러 형태를 가질 수 있음을 뜻함
> 상속을 이용하여 기능을 확장, 변경하는 것도 다형성임
> 대표적으로 오버라이딩과 오버로딩이 있음
> (하지만 오버로딩은 파이썬에서 지원하지 않음)

#### 오버라이딩
> 부모클래스에 있는 메소드를 자식클래스에서 재정의하는 것
> 자식클래스에서 정의된 메소드가 부모클래스 메소드를 덮어버림
> 부모클래스의 메소드에 다른 기능을 추가하고 싶을 때 사용하면 좋음

## OOP 기본 문법
> 클래스는 붕어빵 틀, 객체는 붕어빵!!
> 클래스로 객체(인스턴스)를 찍어낼 수 있음

### 클래스 & 인스턴스
> **파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스!**
- 클래스: 객체들의 분류
- 인스턴스: 하나하나의 실체/ 예

```python
class MyClass:
    pass    # pass는 구현을 미룰 때 쓰는 것

# 인스턴스 생성
my_instance = MyClass()
# 메소드 호출
my_iinstance.my_method()
# 속성
my_instance.my_attribute
```

```python
class Person:
    pass

print(type(Person))
# type
p1 = Person()
print(type(p1))
# __main__.Person
isinstance(person1, Person)
# True
```
### 속성
- 특정 데이터 타입/ 클래스의 객체들이 가지게 될 **상태/ 데이터**를 의미함

```python
class Person:
    def __init__(self, name):
        self.name = name
        
person1 = Person('선영')
person1.name
# 선영
```

### 메소드
- 특정 데이터 타입/ 클래스의 객체에 공통적으로 적용 가능한 **행위(함수)** 를 의미함

```python
class Person:
    def talk(self):
        print('안녕!')
        
    def eat(self, food):
        print(f'{fodd}을 냠냠')
        
person1 = Person()
person1.talk()
person1.eat('엽떡')
# 안녕!
# 엽떡을 냠냠
```
### 객체 비교하기
- ==
    - 동등한(equal)
    - 변수가 참조하는 **객체의 내용(값)이 같은 경우** True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다는 것은 아님
- is
    - 동일한(identical)
    - 두 변수가 **동일한 객체**를 가리키는 경우 True

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)
# True False

a = [1, 2, 3]
b = a

print(a == b, a is b)
# True True
```

## 인스턴스 변수와 메소드
### 인스턴스 변수
- 인스턴스가 가지고 있는 속성(attribute)
- 각 인스턴스들의 고유한 변수
- 생성자 메소드에서 `self.<name>`으로 정의
- 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당

```python
class Person:
    def __init__(self, name):
        self.name = name    # 인스턴스 변수 정의
        
 # 인스턴스 변수 접근 및 할당
john = Person('john')    
print(john.name)
# john
john.name = 'John Kim'
print(john.name)
# John Kim
```

### 인스턴스 메소드
- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
- 클래스 내부에 정의되는 메소드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)가 전달됨

```python
class MyClass:
    def instance_method(self, arg1, ...)
    
my_instance = MyClass()
my_instance.instance_method(...)
```

### self
- 인스턴스 자기자신
- 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
- -> 다른 단어로 써도 작동은 하지만 암묵적인 규칙이므로 그냥 self로 쓰자

### 생성자 메소드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 인스턴스 변수들의 초기값을 설정

```python
class Person:
    def __init__(self):
        print('인스턴스 생성')
        print('이것은 생성자 메소드!')
        
person1 = Person()
# 인스턴스 생성
# 이것은 생성자 메소드!
```
```python
class Person:
    def __init__(self, name):
        print(f'{name} 인스턴스 생성')
        
person1 = Person('선영')
# 선영 인스턴스 생성
```

### 소멸자 메소드
- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

```python
class Person:
    def __del__(self):
        print('인스턴스 소멸')
        
person1 = Person()
del person1
# 인스턴스 소멸
```