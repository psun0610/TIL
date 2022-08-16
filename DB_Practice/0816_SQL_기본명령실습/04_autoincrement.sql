-- PK컬럼에 AUTOINCREMENT 속성을 주면, 마지막 값을 삭제하고 다시 집어넣었을 때 새로운 값이 들어감
CREATE TABLE members(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

INSERT INTO members VALUES
(1, '홍길동'), 
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

DELETE FROM members where rowid = 5;
INSERT INTO members (name) VALUES ('박선영');
SELECT * FROM members;
-- id  name
-- --  ----
-- 1   홍길동
-- 2   김철수
-- 3   이호영
-- 4   박민희
-- 6   박선영