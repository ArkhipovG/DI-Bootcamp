SELECT 
    genre_name,
    movie_title,
    release_date
FROM (
    SELECT 
        g.genre_name,
        m.title AS movie_title,
        m.release_date,
        FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie
    FROM 
        movies.movie_genres mg
    JOIN 
        movies.movie m ON mg.movie_id = m.movie_id
    JOIN 
        movies.genre g ON mg.genre_id = g.genre_id
) subquery
WHERE 
    movie_title = most_recent_movie
ORDER BY 
    genre_name;
