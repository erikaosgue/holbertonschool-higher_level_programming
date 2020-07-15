--  No Comedy tonight!
-- lists all shows without the genre Comedy in the database
SELECT title
FROM tv_shows ts 
WHERE title NOT IN(
    SELECT title 
    FROM tv_genres tg 
    JOIN tv_show_genres tsg ON tg.id = tsg.genre_id 
    JOIN tv_shows ts ON tsg.show_id = ts.id
    WHERE name = 'Comedy')
ORDER BY title;
