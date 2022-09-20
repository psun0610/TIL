# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
name_list = ['봉준호', '김한민', '최동훈', '이정재', '이경규', '한재림', 'Joseph Kosinski', '김철수']
debut_list = ['1993-01-01', '1999-01-01', '2004-01-01', '2022-01-01', '1992-01-01', '2005-01-01', '1999-01-01', '2022-01-01']
country = 'KOR'

for i in range(8):
    Director.objects.create(name = name_list[i], debut = debut_list[i], country = country)
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
title_list = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']
for i in range(9):
    genre = Genre()
    genre.title = title_list[i]
    genre.save()
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
for obj in Director.objects.all():
    print(obj.name, obj.debut, obj.country)
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
data = Director.objects.get(id=4)
print(data.name, data.debut, data.country)
# 테이블에 다른 값들을 넣었다가 삭제했더니 id가 4부터 시작하네요 ㅎㅎ;
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
data = Director.objects.get(country = 'USA')
print(data.name, data.debut, data.country)
# 오류발생
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
get 메소드는 무조건 값이 하나가 있어야 성립되고 만약 값이 없거나 2개 이상이라면 오류를 발생한다.
Director의 country에는 USA 값이 하나도 없기 때문에 오류가 발생한다.
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
data = Director.objects.get(name = 'Joseph Kosinski')
data.country = 'USA'
data.save()
print(data.name, data.debut, data.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
data = Director.objects.get(country = 'KOR')
print(data.name, data.debut, data.country)
# 오류발생
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
> 

```
get 메소드는 무조건 값이 하나가 있어야 성립되고 만약 값이 없거나 2개 이상이라면 오류를 발생한다.
이번에는 값이 7개가 return돼서 너무 많은 값이 리턴되었기 때문에 오류가 발생한다.
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
data = Director.objects.filter(country='KOR')
for d in data:
    print(d.name, d.debut, d.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get은 하나의 값만 찾을 수 있기 때문에 Primary Key로 값을 조회할 때 쓰면 좋을 것 같고, filter는 0개든 1개든 100개든 모두 찾을 수 있는 iterable한 그룹을 리턴해주기 때문에 sql문에서 WHERE을 쓰듯이 사용하면 좋을 것 같다.
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
data = Director.objects.get(name='김철수')
data.delete()
```