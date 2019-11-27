-- list all shows contained in the database
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS "number_of_shows"
FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY "number_of_shows" DESC;
