SELECT 
    g.genre_name,
    m.title,
    m.budget,
    SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_budget
FROM 
    movies.movie_genres mg
JOIN 
    movies.movie m ON mg.movie_id = m.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name, m.title;
