### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT *
FROM playlist_track AS 'A'
ORDER BY playlistId DESC
LIMIT 5;
```
```
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT *
FROM tracks AS 'B'
ORDER BY TrackId ASC
LIMIT 5;
``` 
```
TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  Bytes     UnitPrice
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  --------  ---------
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99

2        Balls to the Wall                        2        2            1                                                                      342562        5510424   0.99

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99
```
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT playlist_track.PlaylistId,
       tracks.Name
FROM tracks
JOIN playlist_track
ON tracks.TrackId = playlist_track.TrackId
ORDER BY playlist_track.PlaylistId DESC
LIMIT 10;
```
```
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT playlist_track.PlaylistId, tracks.Name
FROM tracks
JOIN playlist_track
ON tracks.TrackId = playlist_track.TrackId
WHERE PlaylistId = 10
ORDER BY tracks.Name DESC
LIMIT 5;
``` 
```
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks
INNER JOIN artists
ON tracks.Composer = artists.Name;
```
```
COUNT(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks
LEFT JOIN artists
ON tracks.Composer = artists.Name;
```
```
COUNT(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
inner join은 tracks의 Composer과 artists의 Name이 모두 NULL이 아닐 때 (값이 있을 때)만 출력되고,
left join은 artists의 Name에 값이 없어도 tracks의 Composer의 값이 모두 출력되기 때문에 행의 개수가 다르다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;
``` 
```
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
``` 
```
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId DESC
LIMIT 5;
``` 
```
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2239           411
2238           411
2237           411
2236           411
```

### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT invoices.InvoiceId, customers.CustomerId
FROM invoices
JOIN customers
ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
``` 
```
InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT invoice_items.InvoiceLineId, invoice_items.InvoiceId, customers.CustomerId
FROM invoice_items
  JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
  JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;
```
```
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT invoices.CustomerId, COUNT(*)
FROM invoice_items
  JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
GROUP BY invoices.CustomerId
ORDER BY invoices.CustomerId
LIMIT 5;
```

```
CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```


