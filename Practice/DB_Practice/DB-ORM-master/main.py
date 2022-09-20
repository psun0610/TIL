import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.
name_list = ['봉준호', '김한민', '최동훈', '이정재', '이경규', '한재림', 'Joseph Kosinski', '김철수']
debut_list = ['1993-01-01', '1999-01-01', '2004-01-01', '2022-01-01', '1992-01-01', '2005-01-01', '1999-01-01', '2022-01-01']
country = 'KOR'

for i in range(8):
    Director.objects.create(name = name_list[i], debut = debut_list[i], country = country)

# 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.
title_list = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']
for i in range(9):
    genre = Genre()
    genre.title = title_list[i]
    genre.save()

# 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.
for obj in Director.objects.all():
    print(obj.name, obj.debut, obj.country)

# 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.
data = Director.objects.get(id=4)
print(data.name, data.debut, data.country)

# 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.
data = Director.objects.get(country = 'USA')
print(data.name, data.debut, data.country)

# 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서
# `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.
data = Director.objects.get(name = 'Joseph Kosinski')
data.country = 'USA'
data.save()
print(data.name, data.debut, data.country)

# 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.
data = Director.objects.get(country = 'KOR')
print(data.name, data.debut, data.country)

# 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.
data = Director.objects.filter(country='KOR')
for d in data:
    print(d.name, d.debut, d.country)

# 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.
data = Director.objects.get(name='김철수')
data.delete()

# 15
import re
data = Director.objects.filter(country='KOR', debut='2022-01-01 00:00:00')
# data = Director.objects.filter(country='KOR', re.match('2022', debut))

for d in data:
    print(d.name, d.debut, d.country)

# values()를 하면 딕셔너리로 바꿔줌! -> iterable
for obj in Director.objects.all().values():
    l = [*obj]
    for field in l:
        print(obj[field])
        print()