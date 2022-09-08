-- list all shows from hbtn_0d_tvshows' by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show.id = tv_show_ratings.show_id
GROUP BY tv_show_ratings.id
ORDER BY rating DESC;
