WITH director_ratings AS (
    SELECT 
        p.person_name AS director_name,
        AVG(m.vote_average) AS average_rating,
		COUNT (m.movie_id) AS movie_count
		
    FROM 
        movies.movie_crew mc
    JOIN 
        movies.person p ON mc.person_id = p.person_id
    JOIN 
        movies.movie m ON mc.movie_id = m.movie_id
    WHERE 
        mc.job = 'Director' 
    GROUP BY 
        p.person_name
)

	
SELECT 
    director_name,
    average_rating,
	movie_count
FROM 
    director_ratings
WHERE
	movie_count > 4
ORDER BY 
    average_rating DESC
LIMIT 5;
