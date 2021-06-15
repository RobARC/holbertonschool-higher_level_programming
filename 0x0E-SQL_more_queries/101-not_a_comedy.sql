-- Writw a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT DISTINCT tvs.title
FROM tv_shows AS tvs
WHERE tvs.title NOT IN 
(SELECT tvs.title AS title 
	FROM tv_genres AS tvg 
	INNER JOIN tv_show_genres AS tvsg 
	ON tvsg.genre_id = tvg.id 
	INNER JOIN tv_shows AS tvs 
	ON tvsg.show_id = tvs.id 
	WHERE tvg.name = "Comedy")
ORDER BY title ASC; 
