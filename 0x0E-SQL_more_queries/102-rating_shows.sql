--  Rotten tomatoes
--  lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, sum(rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings tsr 
ON ts.id = tsr.show_id
GROUP BY title
ORDER BY rating desc;
