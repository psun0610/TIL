SELECT * FROM users LIMIT 1;

-- 문자열 합치기||
-- (성 + 이름) 출력, 5명만
SELECT last_name || first_name 이름,
age, country, phone, balance
FROM users
LIMIT 5; 
-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-449  250000


-- 문자열 길이 LENGTH
SELECT
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환


-- 문자열 변경 REPLACE
-- 010-1234-5678 => 01012345678
SELECT
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;
-- first_name  phone          REPLACE(phone, '-', '')
-- ----------  -------------  -----------------------
-- 정호          016-7280-2855  01672802855
-- 경희          011-9854-5133  01198545133
-- 정자          011-4177-8170  01141778170
-- 미경          011-9079-4419  01190794419
-- 영환          011-2921-4284  01129214284


-- 숫자 활용
-- 5, 2 나눈 나머지
SELECT MOD(5, 2)
FROM users
LIMIT 1;
-- MOD(5, 2)
-- ---------
-- 1.0


-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;
-- CEIL(3.14)  FLOOR(3.14)  ROUND(3.14)
-- ----------  -----------  -----------
-- 4.0         3.0          3.0


-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;
-- SQRT(9)
-----
-- 3.0


-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;
-- POWER(9, 2)
-- -----------
-- 81.0