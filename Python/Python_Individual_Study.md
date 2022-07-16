# Python 개별적으로 공부하며 알게된 것들
## print() 함수
> 구글에서 이것저것 검색을 해보다가 `print()` 함수가 단순히 출력만 하는 함수가 아니라는 것을 알게 되었다!
- `print()` 함수의 매개변수
  - sep & end
    `sep`은 받아온 value 사이에 삽입할 문자열을 적어준다.
    `end`는 마지막 value 뒤에 붙이고 싶은 문자열을 적어준다.
    `sep`은 기본값이 ' ', `end`는 기본값이 '\n'이다.

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
    - 버퍼(buffer)란?
      만약 입력된 내용을 바로바로 출력을 시킨다면 엄청난 성능 낭비가 있을 것이다. 이때 버퍼에 잠시 출력될 내용들을 모아놨다가 한 번에 출력하여 효율적으로 작업을 할 수 있게 한다.
      따라서 `flush` 인자를 `True`로 설정해주면 버퍼에 들어오는 값을 모아놨다가 한 번에 출력하는 것이 아니라 버퍼에 들어오는 값들을 들어오자마자 바로 출력 방향으로 밀어 넣을 수 있게 된다.
    ```python
    import time
    
    for i in range(10):
      print(i, end=' ', flush=True)
      time.sleep(1)
    ```
    예를 들어 위의 코드는 `print()`함수가 실행될 때마다 flush가 되어 1초에 한 글자씩 출력된다.

    ```python
    import time

    for i in range(10)
      print(i, end =' ')
      time.sleep(1)
    ```
    파이썬의 end parameter가 `\n`인 경우 내용이 바로 flush 되지만, `' '`인 경우 output이 buffered 상태여서 10초째에 모든 숫자가 동시에 출력된다.
