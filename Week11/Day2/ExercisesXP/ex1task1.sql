SELECT 
    g.genre_name,
    m.title,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
FROM 
    movies.movie m
JOIN 
    movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN 
    movies.genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name, rank;
