-- 단일행 서브쿼리
-- 가장 나이가 작은 사람의 수
-- 방법 1 
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age ASC
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 진짜 맞는지 확인해보자
-- 가장 적은 나이 출력하기
SELECT MIN(age) FROM users;
-- MIN(age)
-- --------
-- 15

-- 방법 2 서브 쿼리 이용
SELECT age, COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 평균 계좌 잔고가 높은 사람의 수 출력
SELECT balance, COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
-- balance  COUNT(*)
-- -------  --------
-- 250000   222

-- 유은정과 같은 지역에 사는 사람의 수 출력
SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name = '유' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 101

-- 전체 인원과 평균 연봉, 평균 나이 출력
-- 방법 1
SELECT COUNT(*), AVG(balance), AVG(age) FROM users;
-- COUNT(*)  AVG(balance)  AVG(age)
-- --------  ------------  --------
-- 1000      151456.89     27.346

-- 방법 2 SELECT에서 서브쿼리 이용
-- 이런 방법은 테이블이 여러 개 있을 때 이용하면 좋음!
-- 예를 들어 댓글 테이블, 게시글 테이블이 있으면 총 댓글 수, 총 게시글 수를 한번에 출력하고 싶을 때 사용할 수 있음
SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉,
    (SELECT AVG(age) FROM users) AS 평균나이;
-- 총인원   평균연봉       평균나이
-- ----  ---------  ------
-- 1000  151456.89  27.346

-- 다중행 서브쿼리
-- 이은정과 같은 지역에 사는 사람의 수
SELECT
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도
-- 전라북도 이은정과 경상북도 이은정으로 나뉘기 때문에 이를 합쳐서 출력해야함

SELECT country, COUNT(*) FROM users GROUP BY country;
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115

-- 아래처럼 하면 전라북도에 사는 사람의 수만 집계된다.
SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 115

-- 이렇게 다중행 서브쿼리를 처리할 때에는 아래처럼 IN을 써주면 된다.
SELECT COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218

-- 특정 성씨별로 가장 적은 나이의 사람들의 이름과 나이
SELECT
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;
-- last_name  MIN(age)
-- ---------  --------
-- 강          15
-- 고          15
-- 곽          15
-- 구          17
-- 권          16
-- 김          15
-- 나          17
-- 남          17
-- 노          16
-- 류          15
-- 문          16
-- 민          18
-- 박          15
-- 배          19
-- 백          17
-- 서          19
-- 성          15
-- 손          16
-- 송          16
-- 신          26
-- 심          22
-- 안          16
-- 양          16
-- 엄          15
-- 오          15
-- 우          17
-- 유          15
-- 윤          16
-- 이          15
-- 임          24
-- 장          15
-- 전          19
-- 정          15
-- 조          22
-- 주          16
-- 지          15
-- 진          16
-- 차          15
-- 최          15
-- 하          16
-- 한          15
-- 허          16
-- 홍          15
-- 황          16

SELECT last_name, first_name, age
FROM users
WHERE (last_name, age) in (SELECT last_name, MIN(age) FROM users GROUP BY last_name)
ORDER BY last_name;
-- last_name  first_name  age
-- ---------  ----------  ---
-- 강          정수          15
-- 고          우진          15
-- 고          시우          15
-- 곽          현숙          15
-- 구          성현          17
-- 권          수빈          16
-- 권          지훈          16
-- 권          성호          16
-- 김          서영          15
-- 김          지훈          15
-- 김          주원          15
-- 김          예준          15
-- 김          예준          15
-- 김          서영          15
-- 김          진우          15
-- 김          재호          15
-- 김          민지          15
-- 김          정숙          15
-- 김          정식          15
-- 나          은정          17
-- 남          예은          17
-- 남          명자          17
-- 노          정숙          16
-- 류          승민          15
-- 문          유진          16
-- 문          동현          16
-- 문          현정          16
-- ...