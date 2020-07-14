-- Temperatures #1
-- A script that displays the top 3 of cities temperature during July and August 
-- ordered by temperature (descending)
SELECT city, avg(value) AS avg_temp
FROM temperatures
WHERE month in (7,8)
GROUP BY city
ORDER BY avg(value) DESC
LIMIT 3;
