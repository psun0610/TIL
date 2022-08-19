-- 단순 조회
SELECT id, gender FROM healthcare LIMIT 5;
-- id  gender
-- --  ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2

-- 성별 1은 남자로, 성별 2는 여자로 바꾸기
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
        -- ELSE
    END AS '성별'
FROM healthcare
LIMIT 5;
-- id  성별
-- --  --
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자

-- 흡연자, 비흡연자로 나누기
SELECT id, smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '금연중'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 15;
-- id  smoking  CASE
-- --  -------  ----
-- 1   1        비흡연자
-- 2   1        비흡연자
-- 3   1        비흡연자
-- 4   1        비흡연자
-- 5   1        비흡연자
-- 6   3        금연중
-- 7   3        금연중
-- 8   3        금연중
-- 9   1        비흡연자
-- 10  1        비흡연자
-- 11  1        비흡연자
-- 12  3        금연중
-- 13  3        금연중
-- 14  1        비흡연자
-- 15  1        비흡연자

-- 나이에 따라 구분
-- 청소년(~18), 청년(~30), 중장년(~90)
SELECT
    first_name,
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 30 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년'
    END
FROM users
LIMIT 10;
-- first_name  last_name  age  CASE
-- ----------  ---------  ---  ----
-- 정호          유          40   중장년
-- 경희          이          36   중장년
-- 정자          구          37   중장년
-- 미경          장          40   중장년
-- 영환          차          30   청년
-- 서준          이          26   청년
-- 주원          민          18   청소년
-- 예진          김          33   중장년
-- 서현          김          23   청년
-- 서윤          오          22   청년