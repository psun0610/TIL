-- SQLite
-- classmates
-- name : TEXT
-- age : INT
-- address : TEXT

-- 테이블 생성
-- [필드 이름] [타입] [제약 조건]
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- PRIMARY KEY => 유일한 값
-- NOT NULL => 비어있는 것을 허용하지 않음
-- DEFAULT 1 => 기본 값은 1 (age값이 주어지지 않았을 때 1이 자동으로 들어감)
-- CHECK (0 < age) => age값이 0보다 커야함

-- CREATE TABLE students(
-- id INTEGER PRIMARY KEY,
-- name TEXT NOT NULL,
-- age INTEGER DEFAULT 1 CHECK (0 < age)
-- );


-- INSERT INTO classmates VALUES ('홍길동', 23);
-- Parse error: table classmates has 3 columns but 2 values were supplied

-- 총 3개의 필드 중 2개에만 값을 넣을 거라면 (name, age)처럼 필드를 직접 지정해줘야 한다.
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;

-- 모든 필드 요소를 다 넣을 거면 (name, age, address)처럼 필드를 따로 지정해줄 필요는 없다.
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

SELECT rowid, * FROM classmates;
-- rowid는 SQLite에서 자동으로 제공하고 있는 PK(Primary Key),
-- 값이 1씩 증가하는 모습을 보임