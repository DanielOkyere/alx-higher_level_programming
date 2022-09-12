-- Use 'hbtn_0d_tvshows' to list all genres not linked to show 'Dexter'
-- 'tv_shows' table containes only one record while title = Dexter
-- Each record should display tv_genres.name
-- Results must be sorted ascending order by genre name
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
      SELECT g.name
      FROM tv_genres g
      INNER JOIN tv_show_genres m ON g.id = m.genre_id
      INNER JOIN tv_show s ON m.show_id = s.id
      WHERE s.title = 'Dexter'
)
ORDER BY g.name;
