-- SQLite
-- csv 파일 examples 테이블의 값으로 한 번에 받아오기
.mode csv
.import hellodb.csv examples

-- examples 테이블 전체 조회
SELECT * FROM examples;

-- id, first_name ... 등 헤더도 함께 조회할 수 있음
.headers ON

-- 행에 예쁘게 줄을 그어줌 (---)
.mode COLUMN
SELECT * FROM examples;