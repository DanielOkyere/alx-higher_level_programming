-- not in my genres
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
      SELECT g.name
      FROM tv_genres g
      INNER JOIN tv_show_genres m ON g.id = m.genre_id
      INNER JOIN tv_show s ON m.show_id = s.id
      WHERE s.title = 'Dexter'
) ORDER BY g.name ASC;
