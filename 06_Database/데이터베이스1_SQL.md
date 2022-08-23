# Database

> 체계화된 데이터의 모임
>
> 몇 개의 자료 파일을 **조직적으로 통합**하여 자료 항목의 중복을 없애고 자료를 **구조화**하여 기억시켜 놓은 자료의 집합체



## 데이터베이스로 얻는 장점

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보 보장)
- 데이터 일관성
- 데이터 독립성 (물리적/ 논리적)
- 데이터 표준화
- 데이터 보안 유지



# RDB (Relational Database)

> 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터 베이스 유형
>
> 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스



## 스키마 (schema)

> 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

| column  | datatype |
| :-----: | :------: |
|   id    |   INT    |
|  name   |   TEXT   |
| address |   TEXT   |
|   age   |   INT    |



## 테이블 (table)

> 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
>
> 스키마를 기반으로 작성됨

- **열, 컬럼, 필드**: 각 열에 고유한 데이터 형식 지정
- **행, 로우, 레코드**: 실제 데이터가 저장되는 형태
- **기본키 (Primary Key, PK)**: 각 레코드의 고유 값
  - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 정립시 주요하게 활용됨

|  id  |  name  | address | age  |
| :--: | :----: | :-----: | :--: |
|  1   | 홍길동 |  제주   |  20  |
|  2   | 김길동 |  서울   |  30  |
|  3   | 박길동 |  독도   |  40  |



# RDBMS (관계형 데이터베이스 관리 시스템)

> 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템
>
> MySQL, SQLite, ORACLE, PostgreSQL, SQLServer 등이 있음



# SQLite

> 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
>
> 로컬에서 간단한 DB 구성을 할 수 있음



## SQLite Data Type

- NULL
- INTEGER
  - 크기에 따라 0, 1, 2, 3 또는 8바이트에 저장된 부호가 있는 정수
- REAL
  - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
- TEXT
- BLOB
  - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

## SQLite Type Affinity

> 특정 컬럼에 저장하도록 권장하는 데이터 타입
>
> 다른 타입의 데이터 삽입시 컬럼에 맞게 알아서 들어감 (다른 DB에서 사용하는 데이터 타입을 사용해도 무방)

- INTEGER
- TEXT
- BLOB
- REAL
- NUMERIC

![type_affinity](데이터베이스1_SQL.assets/type_affinity.png)

# SQL (Structured Query Language)

> RDBMS의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
>
> 데이터베이스 스키마 생성 및 수정
>
> 자료의 검색 및 관리
>
> 데이터베이스 객체 접근 조정 관리



- DDL (Data Definition Language)
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - ex) CREATE, DROP, ALTER
- DML (Data Maniulation Language)
  - 데이터를 저장, 조회, 수정, 삭제 (CRUD) 등을 위한 명령어
  - ex) INSERT, SELECT, UPDATE, DELETE
- DCL (Data Control Language)
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - ex) GRANT, REVOKE, COMMIT, ROLLBACK



# 테이블 생성 ~ 삭제

## 데이터베이스 생성

```sqlite
sqlite3 tutorial.sqlite3
sqlite> .database
```

이때 `.database`처럼 `.`으로 시작하는 명령어는 sqlite에서만 활용되는 명령어임



## csv 파일을 table로 만들기

```sqlite
sqlite> .mode csv
-- csv 파일을 examples 테이블의 값으로 한 번에 받아오기
sqlite> .import hellodb.csv examples

-- 테이블 만들어졌는지 확인
sqlite> .tables
examples
```



## 테이블 생성 (CREATE)

> 데이터베이스에서 테이블 생성

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
```

### 현재 테이블 조회

```sqlite
.tables
classmates examples
```

### 특정 테이블의 schema 조회

```sqlite
sqlite> .schema classmates
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
    name TEXT
);
```



## 테이블에서 데이터 조회 (SELECT)

```sqlite
sqlite> SELECT * FROM examples;

1, "길동", "홍", 600, "충청도", 010-0000-0000

-- 컬럼명 같이 보여줌
sqlite> .headers on
sqlite> SELECT * FROM examples;
id, first_name, last_name, age, country, phone
1, "길동", "홍", 600, "충청도", 010-0000-0000

-- 컬럼과 구분지어주는 선을 그어주고 보기 좋게 정렬해줌
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  ------------
1   "길동"       "홍"       600  "충청도"  010-0000-0000

SELECT * FROM examples;
```



## 테이블 삭제 (DROP)

```sqlite
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```



## 필드 제약 조건 (스키마 작성시)

- NOT NULL: NULL 값 입력 금지
- UNIQUE: 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
- PRIMARY KEY: 테이블에서 반드시 하나, NOT NULL + UNIQUE
- FOREIGN KEY: 외래키, 다른 테이블의 Key
- CHECK: 조건으로 설정된 값만 입력 허용
- DEFAULT: 기본 설정 값



```sqlite
CREATE TABLE students(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	age INTEGER DEFAULT 1 CHECK (0 < age)
);
```

- `id`컬럼은 정수값을 받고 PK(유일한 값)다.

- `name`컬럼은 문자열을 받고 `NOT NULL`에 의해 비어있는 것을 허용하지 않는다.

- `age`컬럼은 정수값을 받고 `DEFAULT 1`에 의해 기본 값이 1이다. (age값이 주어지지 않았을 때 1로 저장된다)
- `age`컬럼은 `CHECK (0 < age)`에 의해 age값이 0보다 커야 한다.



# CRUD

## CREATE

> INSERT: 테이블에 행 삽입

- 테이블에 단일 행 삽입 (각 value에 맞게 컬럼 작성)

  ```sqlite
  INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  ```

- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

  ```sqlite
  INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
  ```

### practice

> classmate 테이블에 이름이 홍길동이고 나이가 23인 데이터를 넣어보자

```sqlite
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
```



> classmates 테이블에 이름이 홍길동, 나이가 30, 주소가 서울인 데이터 넣어보자

```sqlite
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
```

이때는 모든 컬럼의 값을 다 지정해줬기 때문에 위의 문제처럼 컬럼명을 따로 지정해주지 않아도 된다.



## Primary Key를 따로 지정해주지 않아도 괜찮을까?

> 아래처럼 PK가 없다면?

```sqlite
sqlite> SELECT * FROM classmates;
name       age        address
---------  ---------  ----------
홍길동		  23
홍길동		  30		 서울
```

### rowid

> SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼

```sqlite
sqlite> SELECT rowid, * FROM classmates;
rowid     name       age        address
--------  ---------  ---------  ----------
1         홍길동		  23
2         홍길동		  30		 서울
```



## READ

> SELECT: 테이블에서 데이트 조회
>
> 다양한 절과 함께 사용 (ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...)

- LIMIT
  - 쿼리에서 **반환되는 행 수를 제한**
  - 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함
- OFFSET
  - 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
  - `SELECT * FROM MYTABLE LIMIT 10 OFFSET 5`: 5개를 건너띄고 6번째 행부터 10개 출력
- WHERE
  - 쿼리에서 반환된 행에 대한 특정 검색 **조건을 지정&**
- SELECT DISTINCT
  - 조회 결과에서 중복 행을 제거함
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성



### practice

> classmates 테이블에서 id, name 컬럼 값만 조회하세요

```sqlite
SELECT rowid, name FROM classmates;
rowid name
----- ----
1     홍길동
2     김철수
3     이호영
4 	  박민희
5	  최혜영
```



> classmates 테이블에서 id, name 컬럼 값을 하나만 조회하세요

```sqlite
SELECT rowid, name FROM classmates LIMIT 1;
rowid name
----- ----
1     홍길동
```



> classmates 테이블에서 id, name 컬럼 값을 세 번째에 있는 하나만 조회하세요

```sqlite
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid name
----- ----
3     이호영
```



> classmates 테이블에서 컬럼 값 중에 주소가 서울인 경우의 데이터를 조회하세요

```sqlite
SELECT * FROM classmates WHERE address = '서울';
name  age  address
----  ---  -------
홍길동  30  서울
```



> classmates 테이블에서 age값 전체를 중복없이 조회하세요

```sqlite
SELECT DISTINCT age FROM classmates;
age
---
30
26
29
28
```

