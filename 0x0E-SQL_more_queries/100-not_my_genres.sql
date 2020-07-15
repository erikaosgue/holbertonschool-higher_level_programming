-- Not my genre
--  list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN (
    SELECT tg.name
    FROM tv_shows ts 
    JOIN tv_show_genres tsg ON ts.id = tsg.show_id
    JOIN tv_genres tg ON tsg.genre_id = tg.id
    WHERE ts.title = 'Dexter');
