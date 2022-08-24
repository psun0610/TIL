# 기본 함수와 연산

## 문자열 함수

- `SUBSTR(문자열, start, length)`: 문자열 자르기
  - 시작 인덱스: 1, 마지막 인덱스: -1
- `TRIM(문자열)`, `LTRIM(문자열)`, `RTRIM(문자열)`: 문자열 공백 제거
- `LENGTH(문자열)`: 문자열 길이
- `REPLACE(문자열, 패턴, 변경값)`: 패턴에 일치하는 부분 변경
- `UPPER(문자열)`, `LOWER(문자열)`: 대소문자 변경
- `||`: 문자열 합치기



## 숫자 함수

- `ABS(숫자)`: 절댓값
- `SIGN(숫자)`: 부호 (양수 1, 음수 -1, 0 0)
- `MOD(숫자1, 숫자2)`: 숫자1을 숫자2로 나눈 나머지
- `CEIL(숫자)`, `FLOOR(숫자)`, `ROUND(숫자, 자리)`: 올림, 내림, 반올림
- `POWER(숫자1, 숫자2)`: 숫자1의 숫자2 제곱
- `SQRT(숫자)`: 제곱근



## 산술 연산자

- `+`, `-`, `*`, `/`와 같은 산술 연산자와 우선 순위를 지정하는 `()` 기호를 연산에 활용할 수 있다.



# GROUP BY

> SELECT 문의 optional 절
>
> 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
>
> **집계 함수**와 활용하였을 때 의미가 있음!
>
> GROUP BY의 결과는 **정렬되지 않음**
>
> **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함**
>
> `SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;`



## ALIAS

> 컬럼명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때 ALIAS 활용
>
> AS를 생략하고 공백으로 표현할 수도 있음
>
> 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기
>
> `SELECT last_name AS 성 FROM users;`
>
> `SELECT last_name 성 FROM users;`



## HAVING

> 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음
>
> (실행 순서가 WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문)
>
> 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING 활용
>
> `SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2 HAVING 그룹 조건;`



## practice

> users에서 각 성(last_name)씨가 몇 명씩 있는지 조회

```sqlite
SELECT COUNT(*) FROM users GROUP BY last_name;
```



> 100번 이상 등장한 성만 출력

```sqlite
-- GROUP BY + WHERE 사용하면 오류 발생!
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP
--                                       error here ---^
```



```sqlite
SELECT last_name, COUNT(last_name)
FROM users
GROUP last_name
HAVING COUNT(last_name) >= 100;
-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268
-- 이          179
```



# SELECT 문장 실행 순서

> FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY
>
1. FROM 테이블을 대상으로

2. WHERE 제약 조건에 맞춰서 뽑아서
3. GROUP BY 그룹화한다.
4. HAVING 그룹 중에 조건과 맞는 것만을
5. SELECT 조회하여
6. ORDER BY 정렬하고
7. LIMIT/ OFFSET 특정 위치의 값을 가져온다.

```sqlite
SELECT 컬럼명
FROM 테이블명
WHERE 조건식
GROUP BY 컬럼 혹은 표현식
HAVING 그룹조건식
ORDER BY 컬럼 혹은 표현식
LIMIT 숫자 OFFSET 숫자;
```



# ALTER TABLE

> 테이블 이름 변경
>
> 새로운 column 추가
>
> column 이름 수정
>
> column 삭제

```sqlite
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 컬럼 추가
ALTER TABLE table_name
ADD COLUMN column_definition;

-- 3. 컬럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

-- 4. 컬럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
```



## practice

> title과 content 컬럼을 가진 articles라는 이름의 table을 새로 만들기 (두 컬럼 모두 비어 있으면 안되며, rowid 사용)

```sqlite
CREATE TABLE articles (
	title TEXT NOT NULL,
    content TEXT NOT NULL
);
```



> articles 테이블에 값 추가하기 (title은 '1번제목', content는 '1번내용')

```sqlite
INSERT INTO articles VALUE ('1번제목', '1번내용');
```



> 테이블 이름 변경하기

```sqlite
ALTER TABLE articles RENAME TO news;
```



> 새로운 컬럼 추가하기: 새로운 컬럼 이름은 created_at, TEXT 타입에 NULL 허용 X

❗ 아래처럼 NOT NULL 적용을 하면 ERROR!

테이블에 있던 기존 레코드들은 새로 추가할 필드에 대한 정보가 없기 때문에 NOT NULL 형태의 컬럼은 추가할 수 없다

```sqlite
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
```

=> NOT NULL 설정 없이 추가하기 (기존 레코드들에는 값이 비어있음)

```sqlite
ALTER TABLE news ADD COLUMN created_at TEXT;
```

```
sqlite> SELECT * FROM news;
title	  content	  created_at
--------  ----------  ----------
1번제목	  1번내용
제목			내용		2021-06-03
```



=> 혹은 기본 값(DEFAULT) 설정해주기 (기본 값으로 설정됨)

```sqlite
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
```

```
sqlite> SELECT * FROM news;
title	  content	  created_at  subtitle
--------  ----------  ----------  --------
1번제목	  1번내용					소제목
제목			내용		2021-06-03   소제목
```

