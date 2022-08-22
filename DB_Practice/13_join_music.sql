SELECT * 
FROM albums JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;
-- AlbumId  Title                                  ArtistId  ArtistId  Name
-- -------  -------------------------------------  --------  --------  ---------
-- 1        For Those About To Rock We Salute You  1         1         AC/DC
-- 2        Balls to the Wall                      2         2         Accept
-- 3        Restless and Wild                      2         2         Accept
-- 4        Let There Be Rock                      1         1         AC/DC
-- 5        Big Ones                               3         3         Aerosmith

SELECT * 
FROM albums LEFT JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;
-- AlbumId  Title                                  ArtistId  ArtistId  Name
-- -------  -------------------------------------  --------  --------  ---------
-- 1        For Those About To Rock We Salute You  1         1         AC/DC
-- 2        Balls to the Wall                      2         2         Accept
-- 3        Restless and Wild                      2         2         Accept
-- 4        Let There Be Rock                      1         1         AC/DC
-- 5        Big Ones                               3         3         Aerosmith