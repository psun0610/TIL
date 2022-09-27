# ORM

> Object-Relational-Mapping
>
> 객체로 DB를 조작하는 기술!

호환되지 않는 유형의 시스템 간의 데이터를 **객체 지향 프로그래밍 언어를 사용하여** 변환하는 프로그래밍 기술

파이썬에는 SQLAlchemy, peewee 등 라이브러리가 있고 Django 프레임워크에서는 내장 Django ORM 활용함

&nbsp;

## 모델 설계 및 반영

### 1. 클래스로 원하는 DB 구조 생성

Genre라는 데이터베이스에 name(char필드, 최대 길이 30)필드를 생성한다.

Primary Key로 id 필드도 자동으로 생성된다.

```python
class Genre(models.Model):
	name = models.CharField(max_length=30)
```

&nbsp;

### 2. 생성한 클래스를 데이터베이스에 반영하기 위한 마이그레이션 파일 생성

`makemigrations`를 통해 데이터베이스 설계도를 만든다.

```bash
$ python manage.py makemigrations
```



### 3. DB에 마이그레이트한다.

`migrate`를 통해 2번에서 만든 설계도를 바탕으로 DB에 등록한다.

```bash
$ python manage.py migrate
```



> ### 📌Migration(마이그레이션)이란?
>
> Model에 생긴 변화를 DB에 반영하기 위한 방법
>
> 마이그레이션 파일을 만들어 DB 스키마를 반영한다.
>
> 1. `makemigrations` : 마이그레이션 파일 생성
> 2. `migrate`: 마이그레이션을 DB에 반영

