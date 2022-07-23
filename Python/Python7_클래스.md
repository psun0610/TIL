# Python(7) 클래스
## 클래스 속성(변수)
- 한 클래스의 모든 인스턴스가 똑같은 값을 갖고 있는 속성
- 클래스 선언 내부에서 정의
- `{class.name}.{name}`으로 접근 및 할당
```python
class Circle:
    pi = 3.14
    
c1 = Circle()
c2 = Circle()

print(Circle.pi)
print(c1.pi)
print(c2.pi)
# 모두 3.14
```
## namespace
> 인스턴스와 클래스 간의 이름 공간
- 클래스를 정의하면, 클래스와 해당하는 namespace 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 namespace 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스->클래스 순으로 탐색!

```python
class Person:
    species = 'human'          # 클래스 속성 정의
    
    def __init(self, name):    # 생성자 함수
        self.name = name       # 인스턴스 변수 정의
    # 클래스 namespace에 __init__ = __init__(self, name)와
    # species = 'human' 저장
        
p1 = Person('Hong')
p2 = Person('Choi')
# p1, p2 각각 인스턴스별 namespace에 name = 'Hong', name = 'Choi' 저장
```
```python
class Person:
    name = 'unknown'
    
    def talk(self):
        print(self.name)
        
p2 = Person()
p2.talk()
# unknown
# 인스턴스 namespace에 name이 없기 때문에 클래스 namespace에서 탐색해서 unknown 출력
p2.name = 'Kim'
p2.talk()
# Kim
# 인스턴스 namespace에 name이 있기 때문에 바로 Kim 출력
```

## 클래스 메소드
- 클래스가 사용할 메소드
- `@classmethod` 데코레이터를 사용하여 정의
    - **데코레이터**: 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

```python
class MyClass:
    # 클래스 메소드 선언
    @classmethod
    def class_method(cls, arg1, ...)
 
# 클래스 메소드 호출
MyClass.class_method(...)
```
## 스태틱 메소드
- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
- 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때, 사용
- `@staticmethod` 데코레이터를 사용하여 정의
- 호출 시, **어떠한 인자도 전달되지 않음** (클래스 정보에 접근/ 수정 불가)

```python
class MyClass:
    # 스태틱 메소드 선언
    @staticmethod
    def static_method(arg1, ...)
    
# 스태틱 메소드 호출
MyClass.static_method(...)
```

## 객체지향 프로그래밍의 특징
### 추상화
> 데이터나 기능을 의미나 수행과정이 비슷한 개념으로 묶어 정의(선언)하는 것
```python
# 학생을 표현하기 위한 클래스 생성
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
    def talk_age(self):
        print(f'제 나이는 {self.age}입니다.')
    
# 교수를 표현하기 위한 클래스 생성
class Professor:
    def __init__(self, name, age, department, gpa):
        self.name = name
        self.age = age
        self.department = department
        self.gpa = gpa
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
    def teach(self):
        self.age += 1
```

### 상속
> 기존의 클래스를 상속받아 새로운 기능을 추가한 새로운  클래스를 만들 수 있음
> 이때 기존 클래스는 부모클래스(슈퍼클래스), 상속받은 클래스는 자식클래스(서브클래스)

```python
class ChildClass(ParentClass):
    pass
```
- 모든 파이썬 클래스는 object를 상속받음
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건등 **모든 요소**를 상속받음
- 부모 클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
- 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 namespace는 `인스턴스 -> 자식 클래스 -> 부모 클래스` 순으로 탐색
- 다중 상속
    - 두개 이상의 클래스를 상속 받는 경우
    - 상속 받은 모든 클래스의 요소를 활용 가능함
    - 중복된 속성이나 메소드가 있는 경우 상속 순서에 의해 결정

#### 상속: 메소드, 속성의 재사용
```python
class Person:
name = '이름'
age = '나이'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name):
        self.name = name

sunyoung = Student(name='선영')
print(sunyoung.name)
# 선영
sunyoung.talk()
# 반갑습니다. 선영입니다.
# Student 클래스에 없지만 부모 클래스인 Person 클래스의 메소드가 실행됨
# 메소드의 재사용!
print(sunyoung.age)
# 나이
# Student 클래스에 없는 속성이라서 부모 클래스인 Person 클래스의 속성인 age = '나이' 가 출력됨
# 속성 제사용!
```
#### 상속 관련 함수와 메소드
1. `isintance({object}, {classinfo})`
- *classinfo*의 instance거나 **subclass**인 경우 True

- **상속이 없는 경우**
```python
class Person:
    pass
class Professor:
    pass
class Student:
    pass

# 인스턴스 생성
p1 = Professor()
s1 = Student()

print(isinstance(p1, Person))
# False
print(isinstance(p1, Prefessor))
# True
print(isinstance(p1, Student))
# False
print(isinstance(s1, Person))
# False
print(isinstance(s1, Professor))
# False
print(isinstance(s1, Student))
```
- **상속인 경우**
```python
class Person:
    pass
class Professor(Person):
    pass
class Student(Pserson):
    pass

# 인스턴스 생성
p1 = Professor()
s1 = Student()

print(isinstance(p1, Person))        # Person을 상속 받았으므로 True
# True
print(isinstance(p1, Prefessor))
# True
print(isinstance(p1, Student))
# False
print(isinstance(s1, Person))        # Person을 상속 받았으므로 True
# True
print(isinstance(s1, Professor))
# False
print(isinstance(s1, Student))
```
2. `issubclass({class},{classinfo}`
- class가 classinfo의 subclass면 True
- classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사함
```python
issubclass(bool, int)
# True
issubclass(float,int)
# False
issubclass(Professor, Person)
# True
issubclass(Professor, (Person, Student))
# True
```
3. `super()`
- 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

- super 사용 안 할 때
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id
```

- super 사용할 때
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        
class Student(Person):
    super __init__(self, name, age, number, email, student_id):
        # Person 클래스의 __init__ 메소드 사용
        super().__init__(name, age, numver, email)
        self.student_id = student_id
```

### 다형성
> 하나의 객체가 여러 형태를 가질 수 있음을 뜻함
> 상속을 이용하여 기능을 확장, 변경하는 것도 다형성임
> 대표적으로 오버라이딩과 오버로딩이 있음 (하지만 오버로딩은 파이썬에서 지원하지 않음)
- 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미함
- 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

#### 메소드 오버라이딩
> 부모클래스에 있는 메소드를 자식클래스에서 재정의하는 것
> 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경함
> 부모클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 에 다른 기능을 추가하거나 바꾸고 싶을 때 사용
```python
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
# 자식 클래스 - Professor
class Professor(Person):
    def talk(self):
        print(f'{self.name}일세.')    # superclass의 talk 메소드 변경

# 자식 클래스 - Student
class Student(Person):
    def talk(self):
        super().talk()                 # superclass의 talk 메소드 불러옴
        print(f'저는 학생입니다.')     # 다른 기능 추가
        
p1 = Professor('김교수')
p1.talk()
# 김교수일세.
s1 = Student('이학생')
s1.talk()
# 반갑습니다. 이학생입니다.
# 저는 학생입니다.
```

### 캡슐화
> 파이썬은 캡슐화는 지원(class)하지만 내부 데이터들은 public으로 제공함(protected, private으로 변경 가능)
> 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단하여 정보은닉이 가능함
> 파이썬에서 기능상으로 존재하지 않지만, 관용적으로 사용되는 표현이 있음
> 결합도는 낮을수록, 응집도는 높을수록 좋음!
- 결합도: 메소드가 다른 메소드에 의존하는 정도
- 응집도: 메소드 내부 요소들의 관련 정도

#### 접근제어자 종류
- Public Access Modifier
    - 언더바 없이 시작하는 메소드나 속성
    - 어디서나 호출이 가능, 하위 클래스 override 허용
- Protected Access Modifier
    - **언더바 1개**로 시작하는 메소드나 속성
    - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- Private Access Modifier
    - **언더바 2개**로 시작하는 메소드나 속성
    - 본 클래스 내부에서만 사용이 가능