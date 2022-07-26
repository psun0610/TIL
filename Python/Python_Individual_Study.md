# Python 개별적으로 공부하며 알게된 것들
## print() 함수
> 구글에서 이것저것 검색을 해보다가 `print()` 함수가 단순히 출력만 하는 함수가 아니라는 것을 알게 되었다!
### `print()` 함수의 매개변수
- sep & end
   - `sep`은 받아온 value 사이에 삽입할 문자열을 적어준다.
   - `end`는 마지막 value 뒤에 붙이고 싶은 문자열을 적어준다.
   -  `sep`은 기본값이 ' ', `end`는 기본값이 '\n'이다.

- **file**
    `print()` 함수는 보통 objects를 텍스트 스트림 file로 출력하는 기능을 한다.
    하지만 `file` 인자에 write(string) 메서드가 포함된 파일 객체를 넘겨주면 단순 출력만이 아니라 파일에 내용을 쓰는 것도 가능하다.
    `file`의 초기값은 `sys.stdout`으로 설정되어 있다.
    ```python
    with open('test.txt', 'w') as f:
      print('Hello world', file=f)
    ```
    
- **flush**
    일반적으로 출력의 버퍼링 여부는 file에 의해 정해지지만, `flush`를 `True`로 설정하면 스트림이 강제로 flush(clear)이 가능하다.
    `print()`함수의 출력 값이 buffered 상태 일 때 `flush=True`로 설정해주면 buffered된 출력값을 바로 바로 목적지에 도달시킬 수 있다는 뜻이다.
    `flush`의 초기값은 `False`이다.
    > 버퍼(buffer)란?
    > 만약 입력된 내용을 바로바로 출력을 시킨다면 엄청난 성능 낭비가 있을 것이다. 이때 버퍼에 잠시 출력될 내용들을 모아놨다가 한 번에 출력하여 효율적으로 작업을 할 수 있게 한다.
    > 따라서 `flush` 인자를 `True`로 설정해주면 버퍼에 들어오는 값을 모아놨다가 한 번에 출력하는 것이 아니라 버퍼에 들어오는 값들을 들어오자마자 바로 출력 방향으로 밀어 넣을 수 있게 된다.
    > 예를 들어 아래의 코드는 `print()`함수가 실행될 때마다 flush가 되어 1초에 한 글자씩 출력된다.
   ```python
    import time
    
    for i in range(10):
      print(i, end=' ', flush=True)
      time.sleep(1)
 ```
    
    파이썬의 end parameter가 `\n`인 경우 내용이 바로 flush 되지만, `' '`인 경우 output이 buffered 상태여서 10초째에 모든 숫자가 동시에 출력된다.
   ```python
    import time

    for i in range(10)
      print(i, end =' ')
      time.sleep(1)
   ```

### `print()`함수의 이모저모,,
- 문자열 두개를 합쳐서 출력할 때
   ```python
a = 'hi'
b = 'python'
print(a, b)
print(a + b)
# hi python 띄어쓰기 되어 나옴, sep인자의 기본값이 ' ' 이기 때문!
# hitpython 공백없이 붙어서 나옴
```

## 소수점 자릿수 조절하기
### round()
- `round(반올림하고자 하는 값)`
    - 소수점 첫째자리에서 반올림이 되어 정수로 만듬
   ```python
a = 3.141592
print(round(a))
# 3
```
- `round(반올림하고자 하는 값, 자릿수)`
    - 원하는 자릿수로 소수점을 조절할 수 있음
   ```python
a = 3.141592
print(round(a,3))
# 3.142
```

### format()
> 문자열을 출력할 때 서식 지정자를 사용하여 출력하고자 하는 경우에 사용
- `format(반올림하고자 하는 값, '.@f')`
    - 값을 반올림해서 소수점 @ 자리까지 출력
```python
a = 3.141592
print(format(a,'.2f'))
# 3.14
```
- `'{:.@f} 문자열'.format(값)`
    - 값을 반올림해서 소수점 @ 자리까지 출력
    - 타입이 str임을 주의!
```python
a = 3.141592
a = '{:.2f}'.format(a)
print(a, type(a))
# 3.14 <class 'str'>
```

### f-string
> format과 동일
- `f'문자열{반올림하고자 하는 값:.@f}'`
    - 값을 반올림해서 소수점 @ 자리까지 출력
   ```python
a = 3.141592
a = f'{a:.2f}'
print(a, type(a))
# 3.14 <class 'str'>
```

## float형을 int형으로 변환
### int()
- `int(변환하고자 하는 값)`
    - 소수 부분을 제외한 정수부를 리턴
   ```python
a = 10.562
a = int(a)
print(a)
# 10
```

### round()
> 위에 소수점 자릿수 조절에서 봤던 round() 함수!
- `round(반올림하고자 하는 값)`
    - 소수점 첫째자리에서 **반올림**이 되어 정수로 만듬
   ```python
a = 3.141592
print(round(a))
# 3
```

### math.ceil()
- `math.ceil()`
    - 소수점 첫째자리에서 **올림**하여 정수로 만듬
    - math 라이브러리에서 제공하므로 import 해줘야 함
   ```python
import math

a = 10.562
a = math.ceil(a)
print(a)
# 11

b = -3.14
b = math.ceil(b)
print(b)
# -3
```
### math.floor()
- `math.floor()`
    - 소수점 첫째자리에서 **내림**하여 정수로 만듬
    - math 라이브러리에서 제공하므로 import 해줘야 함
   ```python
import math

a = 10.562
a = math.floor(a)
print(a)
# 10

b = -3.14
b = math.floor(b)
print(b)
# -4
```

## 아스키코드 vs 유니코드
