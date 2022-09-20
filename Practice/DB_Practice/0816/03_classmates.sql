CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울
-- 김철수   30   제주
-- 이호영   26   인천
-- 박민희   29   대구
-- 최혜영   28   전주

-- classmates 테이블에서 rowid와 name 컬럼값만 보여주는데, 이때 처음부터 2개까지만 보여줌
SELECT rowid, name FROM classmates LIMIT 2;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수

-- OFFSET 2를 하면 2개를 뛰어넘어서 3번째부터 보여주는데 LIMIT 1에 의해 3번째의 rowid와 name만 보여줌
-- OFFSET: 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- rowid  name
-- -----  ----
-- 3      이호영

-- WHERE 뒤에는 조건이 들어가서 조건에 부합하는 것만 조회할 수 있음
SELECT * FROM classmates WHERE address='서울';
-- name  age  address
--  ---  -------
-- 홍길동   30   서울

-- DISTINCT는 중복을 제거해줌
SELECT DISTINCT age FROM classmates;

SELECT DISTINCT address FROM classmates;
-- address
-- -------
-- 서울
-- 제주
-- 인천
-- 대구
-- 전주

-- 삭제
DELETE FROM classmates WHERE rowid=5;
SELECT * FROM classmates;

-- 다시 삽입
-- 마지막 값 삭제 후 다른 로우를 다시 삽입하면 rowid는 다시 채워짐
INSERT INTO classmates VALUES ('박선영', 22, '대구');
SELECT rowid, * FROM classmates;
  -- rowid  name  age  address
  -- -----  ----  ---  -------
  -- 1      홍길동   30   서울
  -- 2      김철수   30   제주
  -- 3      이호영   26   인천
  -- 4      박민희   29   대구
  -- 5      박선영   22   대구

-- 만약 중간 값을 삭제하면?
DELETE FROM classmates WHERE rowid = 3;
-- 1|홍길동|30|서울
-- 2|김철수|30|제주
-- 4|박민희|29|대구
-- 5|박선영|22|대구

-- 한 칸 앞으로 당겨지지 않고 그대로 3이 없이 계속 진행
INSERT INTO classmates VALUES ('영희', 30, '부산');
SELECT rowid, * FROM classmates;
-- 1|홍길동|30|서울
-- 2|김철수|30|제주
-- 4|박민희|29|대구
-- 5|박선영|22|대구
-- 6|영희|30|부산

-- LIMIT을 100까지 걸어도 5개밖에 없기 때문에 5개만 조회됨
SELECT rowid, name FROM classmates LIMIT 100;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수
-- 4      박민희
-- 5      박선영
-- 6      영희