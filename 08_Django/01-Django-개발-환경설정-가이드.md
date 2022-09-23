# ✔Django 개발 환경 설정 가이드

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

