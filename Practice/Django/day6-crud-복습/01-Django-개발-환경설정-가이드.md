# ✔Django 개발 환경 설정 가이드

> Django는 1. url로 요청을 받아서 2. 처리하고 3. 응답을 한다.

## 가상환경 생성 및 실행

### 1. 서버를 관리할 디렉토리를 생성함

**[예시]**

```bash
$ mkdir [생성할 디렉토리 이름]
$ cd [생성된 디렉토리]
```

**[실제 명령]**

```bash
$ mkdir test
$ cd ./test
```

&nbsp;

### 2. `venv` 파이썬 모듈을 실행하여 가상환경을 생성함

**[예시]**

```bash
$ python -m venv [가상환경 이름]

$ ls
test-venv/
```

**[실제 명령]**

```bash
$ python -m venv test-venv
```

&nbsp;

### 3. 생성된 가상환경을 실행함

**[예시]**

```bash
$ source [가상환경 이름]/Scripts/activate
(가상환경 이름이 뜸)
```

**[실제 명령]**

```bash
$ source test-venv/Scripts/activate
(test-venv)
```



만약 위 경로가 생각이 나지 않는다면 직접 들어가서 실행할 수 있다.

```bash
$ cd test-venv/
$ ls
Include/ Lib/ pyvenv.cfg Scripts/

$ cd Scripts/
$ ls
activate activate.bat Activate.ps1 deactivate.bat pip.exe* pip3.9.exe* pip3.exe* python.exe* pythonw.exe*

$ source ./activate
(test-venv)

$ cd ../..
```

&nbsp;

## Django LTS 버전 설치

### 4. Django를 설치함

`pip list`를 확인해보고 장고가 설치되어 있지 않다면 장고를 설치한다.

```bash
$ pip list
Package    Version
---------- --------
pip		   22.0.4
setuptools 58.1.0
(test-venv)

$ pip install django==3.2.12
Collecting django==3.2.12
  Downloading Django-3.2.12-py3-none-any.whl (7.9 MB)
     ---------------------------------------- 7.9/7.9 MB 9.7 MB/s eta 0:00:00
Collecting pytz
  Using cached pytz-2022.2.1-py2.py3-none-any.whl (500 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Installing collected packages: pytz, sqlparse, asgiref, Django
Successfully installed Django-3.2.12 asgiref-3.5.2 pytz-2022.2.1 sqlparse-0.4.2
(test-venv)

$ pip list
Package    Version
---------- --------
asgiref    3.5.2
Django     3.2.12
pip        22.0.4
pytz       2022.2.1
setuptools 58.1.0
sqlparse   0.4.2
(test-venv)
```

&nbsp;

## Django 프로젝트 생성

### 5. 프로젝트 생성함

**[예시]**

```bash
$ django-admin startproject [프로젝트 이름] [시작 경로]
```

**[실제 명령]**

```bash
$ django-admin startproject testpjt .
(test-venv)

$ ls
manage.py*  testpjt/  test-venv/
(test-venv)
```

- `test-venv/`: 가상환경
- `testpjt/`: django 프로젝트 파일
- `manage.py`: 서버를 구동하는 파일

&nbsp;

## Django 실행

### 6. 서버를 실행함

```bash
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 21, 2022 - 14:43:13
Django version 3.2.12, using settings 'testpjt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

&nbsp;

### 7. 서버가 실행되고 있는 지 확인하기

웹 브라우저에 `127.0.0.1` 혹은 `localhost:8000`

![](https://raw.githubusercontent.com/psun0610/Image-upload/image/img/django-rocket.png)

## 가상환경 종료하는 방법

```bash
$ deactivate
```



## 가상환경 지우는 방법

```bash
$ rm -r [가상환경 이름]
```



## Django app 시작하기 & MTV(MVC)모델

> url을 등록하고, view 함수를 생성하고, template를 만든다.

### 1. Django app 시작

**[예시]**

```bash
python manage.py startapp [앱 이름]
```

**[실제 코드]**

```bash
python manage.py startapp articles
```



### 2. settings.py에 app 등록

**[예시]**

```python
INSTALLED_APPS = [
    '앱 이름',
    ...
]
```

**[실제 코드]**

```python
INSTALLED_APPS = [
    'articles',
    ...
]
```



### 3. urls.py 설정

**[예시]**

```python
from django.urls import path, include
from [앱 이름] import views

urlpatterns = [
    path('index/', [views.view 메소드 이름])				# 1
    path('[보통 앱 이름]', include('[앱 이름].urls')),	# 2
]
```

**[실제 코드]**

```python
from django.urls import path, include
from [앱 이름] import views

urlpatterns = [
    path('index/', views.index				# 1
    path('articles/', include('articles.urls')),	# 2
]
```



### 3-1. 프로젝트 단 말고 앱 단에서 url을 관리하기로 했다면

### 앱 폴더에 urls.py 새로 만들기 + path 작성

**[예시]**

```python
from django.urls import path

app_name = '[앱 이름]'

urlpatterns = [
    path('', views.[요청할 view 이름], name='[이 path의 별명]')
]
```

**[실제 코드]**

```python
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index')
]
```



### 4. views.py에 함수 생성

**[예시]**

```python
from django.shortcuts import render

def [urls.py가 부른 view 함수 이름](request):
    return render(request, '[app_name]/[template이름].html')
```

**[실제 코드]**

```python
from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
```



### 5. templates 폴더 생성 + 앱 이름 폴더 생성 + html 생성

이때 앱 이름 폴더를 생성하는 이유는 앱이 여러 개 있을 때 각각의 앱 폴더에서 templates 폴더를 생성한다고 해도 django는 하나의 templates 폴더로 간주하기 때문에 templates 폴더 안에 각 앱의 이름 폴더를 생성하여 구분해주기 위함이다. 특히 각각의 앱에서 같은 template name을 가지고 있다면 우선순위를 따져서 가장 높은 template만을 보여주기 때문에 주의해야 한다.



# CRUD 기능 구현

> 사용자에게 form을 제공하고 입력 받은 데이터를 처리한다.

## DB에 Model 반영

### 1. models.py에 모델 설계 (DB 스키마 설계)

**[예시]**

```python
class [클래스 이름](models.Model):
    [스키마 작성]
```

**[실제 코드]**

```python
class Article(models.Model):
    title = models.CharFeild(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



### 2. 마이그레이션 파일 생성

```bash
python manage.py makemigrations
```



### 3. DB 반영(migrate)

```bash
python manage.py migrate
```



## CREATE 기능 구현

### 1. HTML form 제공

`form`은 사용자에게 양식을 제공하고

- 값을 받아서(input: name, value)

- 서버에 전송 (form: action)

```html
<form action="{% url 'articles:create' %}" method="POST">	<!-- 앱이름:url이름 -->
  {% csrf_token %}	<!-- POST 요청시 반드시 작성해야함 -->
  {{ article_form.as_p }}
  <input type="submit" value="작성완료">
</form>
```

위처럼 `form action`을 `{% url %}`로 주는 이유는 url 구성이 바뀌어도 일일이 수정하지 않도록 하기 위함임



### 2. view에서 request를 받음

```python
from django.shortcuts import render, redirect
from .models import Article

def create(request):
    # CREATE
    if request.method == 'POST':
        # DB 저장
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')	# index 페이지로 redirect
    # method가 GET이면
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)
```



## READ 기능 구현

### 1. DB에서 읽어오기

> DB에서 게시글을 가져와서, template에 전달

```python
def index(request):
    articles = Article.objects.order_by('-pk')    # 게시글을 가져와서 (최신글이 위로 오게 -pk)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)	    # template에 전달
```

### 2. template에서 보여주기

```html
<h1>게시판</h1>
<a href="{% url 'articles:create' %}">글 작성하기</a>
{% for article in articles %}
  <div>
    <p>{{ article.created_at }} | {{ article.updated_at }}</p>
    <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
  </div>
{% endfor %}
```



## UPDATE 기능 구현

### 1. path 등록

```python
path('<int:pk>/update/', views.update, name='update'),
```



### 2.  method가 GET일때와 POST일때 조건을 나눠 작성

- `GET`일때는 ModelForm을 가져온다.
- `POST`일때는 form으로 받아온 데이터를 저장한다.

```python
def update(request, pk):
    # GET 받아서 CREATE
    # method가 POST일때 수정된 글을 저장
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    # method가 GET일때 
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)
```



### 3. template에서 form을 제공하고 POST 방식으로 보냄

📌 이때 `action`속성을 생략하면 해당 페이지를 요청할 때와 같은 방식으로 처리가 된다.

```html
  <form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="작성완료">
  </form>
```



## DELETE 기능 구현

### 1. path 등록

```python
path('<int:pk>/delete/', views.delete, name='delete'),
```



### 2. DB에서 원하는 데이터를 받아와서 삭제

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

