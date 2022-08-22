-- INNER JOIN
-- 'INNER' 생략 가능
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- name과 title만 출력하기
SELECT
    users.name,
    role.title
FROM users JOIN role
ON users.role_id = role.id;
-- name  title
-- ----  -----
-- 관리자   admin
-- 김철수   staff
-- 이영희   staff

-- 스태프(2)만 출력하기
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
WHERE role.id = 2;
-- WHERE users.role_id = 2 도 같은 결과
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 이름을 내림차순으로 출력하기
SELECT *
FROM users JOIN role
ON users.role_id = role.id
ORDER BY name DESC;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

SELECT *
FROM users INNER JOIN articles
ON users.id = articles.user_id
-- id  name  role_id  id  title  content  user_id
-- --  ----  -------  --  -----  -------  -------
-- 1   관리자   1        1   1번글    111      1
-- 2   김철수   2        2   2번글    222      2
-- 1   관리자   1        3   3번글    333      1
-- 둘 다 값이 있는 것만 출력됨 (4번 글은 user_id 값이 NULL이기 때문에 출력이 안됨)


-------------------------------------------------------------------------------------------------
-- LEFT OUTER JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

-- NULL인 자료 제외하고 출력하기
SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

--------------------------------------------------------------------------------------------------
-- FULL OUTER JOIN
SELECT *
FROM articles FULL OUTER JOIN users
ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444
--                              3   이영희   2

--------------------------------------------------------------------------------------------------
-- CROSS JOIN
SELECT *
FROM users CROSS JOIN role;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student

--------------------------------------------------------------------------------------------------
-- 3개의 테이블 조합
SELECT *
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin