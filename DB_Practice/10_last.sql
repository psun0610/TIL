-- AS/DC의 모든 앨범
-- AC/DC (artists)
-- 앨범(albums)

-- ArtistID 조회
SELECT ArtistId
FROM artists
WHERE Name = 'Nirvana';

-- 서브쿼리
SELECT *
FROM albums
WHERE ArtistId = (SELECT ArtistId FROM artists WHERE Name = 'Nirvana');