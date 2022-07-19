# Python(4) 파이썬의 데이터 구조 - 메서드
## 메서드
> 메서드는 `타입.메서드()`로 호출할 수 있다.
> `input().split()`은 `문자열.split()`, `[1, 2, 3].append(4)`은 `리스트.append(4)` 이처럼 `타입.메서드()`를 이용하여 다양한 명령을 구현할 수 있다.

## 시퀀스(순서가 있는 데이터 구조)
### 문자열
  - 문자열 탐색/ 검증
  | 문법 |            설명             |
| :----: | :-------------------------: |
|   s.find(x)    |   x의 첫 번째 위치를 반환. 없으면, -1을 반환   |
|   s.index(x)   |   x의 첫 번째 위치를 반환. 없으면, 오류 발생  |
|   s.isalpha(x)   |   알파벳 문자 여부  |
|   s.isupper()   |  대문자 여부   |
|   s.islower()   |   소문자 여부   |
|   s.istitle()   |  타이틀 형식 여부(띄어쓰기 앞글자가 모두 upper인지 여부)   |

- 문자열 변경
  | 문법 |            설명             |
  | :----: | :-------------------------: |
  |   s.replace(old, new, *count*) |  바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
  |   s.strip([chars])   |  공백이나 특정 문자를 제거   |
  |   s.split(sep=None), maxsplit=-1   |  공백이나 특정 문자를 기준으로 분리 |
  |   'separator'.join([iterable])  |  구분자로 iterable을 합침   |
  |   s.capitalize()   |  가장 첫 번째 글자를 대문자로 변경 |
  |   s.title()   |   '나 공백 이후를 대문자로 변경   |
  |   s.upper()   |   모두 대문자로 변경  |
  |   s.lower()   |  모두 소문자로 변경  |
  |   s.swapcase()   |  대<->소문자 서로 변경  |
  - `.replace(old, new, *count*)`
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - count를 지정하면 해당 개수만큼만 시행
  - `.strip(chars)`
    - 특정한 문자들을 지정하면 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거함(rstrip)
    - 문자열을 지정하지 않으면 공백을 제거함
  - `split(sep=None, maxsplit=-1)`
    - 문자열을 특정한 단위로 나눠 리스트로 반환함
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
    - maxsplit이 -1인 경우에는 제한이 없음
  - `'separator'.join(iterable)`
    - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐서 문자열을 반환함
    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생

### 리스트
  | 문법 |            설명             |
| :----: | :-------------------------: |
|   L.append(x)   |  리스트 마지막에 항목 x를 추가  |
|   L.insert(i, x)   |  인덱스 i에 x값 추가, i가 리스트 길이보다 큰 경우 맨 뒤에 추가  |
|   L.remove(x)   |  처음으로 나오는 x를 제거/ 항목이 존재하지 않을 경우 ValueError  |
|   L.pop()   |  리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거  |
|   L.pop(i)   |  인덱스 i에 있는 항목을 반환 후 제거  |
|   L.clear(x)   |  모든 항목 삭제  |
|   L.extend(iterable)   |  iterable의 항목을 추가(+=과 같은 기능)  |
|   L.index(x)   |   가장 처음 나온 x값의 index값 반환, 없는 경우 ValueError   |
|   L.index(x, start, end)   |  리스트에 있는 항목 중 가장 왼쪽에 있는 x의 인덱스를 반환  |
|   L.reverse()   |  리스트를 거꾸로 뒤집음, None 반환  |
|   L.sort()   |  리스트 정렬, None 반환 **sorted 함수와 비교할 것**  |
|   L.count(x)   |  x의 개수를 반환  |
  - sorted()함수 VS .sort()
  ```python
  #.sort
  numbers = [3, 2, 5, 1]
  result = numbers.sort()
  print(numbers, result)
  # [1, 2, 3, 5] None (원본이 변경됨)

  #sorted()함수
  numbers = [3, 2, 5, 1]
  result - sorted(numbers)
  print(numbers, result)
  # [3, 2, 5, 1] [1, 2, 3, 5] (정렬된 리스트를 반환, 원본은 변경 없음)
  ```

## 컬렉션(순서가 없는 데이터 구조)
### 세트
  | 문법 |            설명             |
| :----: | :-------------------------: |
|   s.copy()   |  세트의 얕은 복사본을 반환  |
|   s.add(x)   |  항목x가 세트s에 없다면 추가  |
|   s.pop()   |  세트s에서 랜덤하게 항목을 반환하고 해당 항목을 제거, 세트가 비어 있을 경우 KeyError  |
|   s.remove(s)   |  항목x를 세트s에서 삭제  |
|   s.discard(x)   |  항목x가 세트s에 있는 경우, 항목x를 세트s에서 삭제  |
|   s.update(t)   |  세트t에 있는 모든 항목 중 세트s에 없는 항목을 추가  |
|   s.clear()   |  모든 항목 제거  |
|   s.isdisjoint(t)   |   세트s가 세트t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환   |
|   s.issubset(t)   |  세트s가 세트t의 하위 세트인 경우, True 반환  |
|   s.issuperset(t)   |  세트s가 세트t의 상위 세트인 경우, True 반환  |

### 딕셔너리
  | 문법 |            설명             |
| :----: | :-------------------------: |
|   d.clear()   |  모든 항목 제거  |
|   d.keys()   |  딕셔너리 d의 모든 키를 담은 뷰를 반환  |
|   d.values()   |  딕셔너리 d의 모든 값을 담은 뷰를 반환  |
|   d.items()   |  딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환  |
|   d.get(k, v=None)   |  키 k의 값을 반환하는데, k가 d에 없을 경우 v 또는 None을 반환  |
|   d.pop(k)   |  키 k의 값을 반환하고 키 k인 항목을 삭제하는데 k가 없을 경우 KeyError   |
|   d.pop(k, v)   |   키 k의 값을 반환하고 키 k인 항목을 삭제하는데 k가 없을 경우 v 반환   |
|   d.update(other)   |  딕셔너리 d의 값을 매핑하여 업데이트 (덮어씀)  |