# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;
```

```
MAX(height)  MIN(height)  MAX(weight)  MIN(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE height >= 160 and height <= 170;
```

```
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 
> 허리 둘레 스키마가 NOT NULL이 아니라서 그런지 아래처럼 waist에 공백이 들어있다.
> 그래서 공백을 제거하고 나머지 중에서 내림차순 limit 5를 찾아야 한다.
```sql
SELECT * FROM healthcare WHERE is_drinking = 1 ORDER BY waist DESC LIMIT 5;
```

```
id     sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking
-----  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------
15583  11    2       11   155     50             1.2      1.2       103             1        1
20143  11    2       9    170     105            0.5      0.5       156             3        1
45103  41    2       10   155     45             0.8      1.0       106             1        1
52074  41    2       11   165     60                                94              1        1
56063  11    1       9    175     75             1.2      1.2       119             2        1
```

---
```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 and waist != '' ORDER BY waist DESC LIMIT 5;
```

```
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;
```

```
COUNT(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
```

```
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height * height) >= 30;
```

```
COUNT(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight*10000/(height * height) AS BMI FROM healthcare WHERE smoking=3 ORDER BY BMI DESC LIMIT 5;
```

```
id      BMI
------  ---
231431  50
934714  49
722707  48
947281  47
948801  47
```

### 13. 몸무게 끝자리가 5인 사람의 수 출력

```sql
SELECT COUNT(*) FROM healthcare WHERE weight LIKE '%5';
```

```
COUNT(*)
--------
497300
```

### 왼쪽 시력과 오른쪽 시력의 합이 큰 사람 순서대로 6명 출력하기

```sql
SELECT * FROM healthcare ORDER BY va_left + va_right DESC LIMIT 6;
```

```
id     sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking
-----  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------
5249   26    1       16   170     70      84.0   9.9      9.9                       1        0
6554   41    2       10   140     40      68.0   9.9      9.9       110             1        0
7905   45    2       11   135     45      76.0   9.9      9.9       91              1        0
10165  27    1       15   155     65      96.0   9.9      9.9       134             1        1
10448  45    1       11   165     60      76.0   9.9      9.9       119             1        0
12671  47    1       16   150     45      76.0   9.9      9.9       124             1        0
```

### 15. gender이 1인 사람 중에 키에서 100을 뺀 값이 몸무게보다 작은 사람을 키가 큰 순서대로 5명 출력

```sql
SELECT * FROM healthcare WHERE gender = 1 and height - 100 < weight ORDER BY height DESC LIMIT 5;
```

```
id      sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking
------  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------
46642   26    1       9    195     100     95.3   1.5      1.5       114             3        1
219595  28    1       9    195     105     97.0   1.5      1.2       135             2        1
229284  28    1       9    195     105     100.0  1.0      1.0       131             1        1
247257  48    1       9    195     100     93.8   1.5      1.2       122             3        1
255109  11    1       9    195     105     102.0  1.0      1.2       118             1        1
```