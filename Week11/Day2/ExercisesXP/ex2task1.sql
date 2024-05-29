WITH actor_movie_counts AS (
    SELECT 
        p.person_name,
        COUNT(mc.movie_id) AS movie_count
    FROM 
        movies.movie_cast mc
    JOIN 
        movies.person p ON mc.person_id = p.person_id
    GROUP BY 
        p.person_name
)
SELECT 
    person_name,
    movie_count,
    DENSE_RANK() OVER (ORDER BY movie_count DESC) AS rank
FROM 
    actor_movie_counts
ORDER BY 
    rank, person_name;



