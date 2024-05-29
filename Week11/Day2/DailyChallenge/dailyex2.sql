WITH average_movie_rating AS (
    SELECT 
        AVG(vote_average) OVER () AS avg_rating
    FROM 
        movies.movie
	LIMIT 1
),
above_average_movies AS (
    SELECT 
        m.movie_id,
        m.vote_average,
        amr.avg_rating
    FROM 
        movies.movie m,
        average_movie_rating amr
    WHERE 
        m.vote_average > amr.avg_rating
),
actor_movie_counts AS (
    SELECT 
        p.person_name,
        COUNT(mc.movie_id) AS movie_count
    FROM 
        above_average_movies aam
    JOIN 
        movies.movie_cast mc ON aam.movie_id = mc.movie_id
    JOIN 
        movies.person p ON mc.person_id = p.person_id
    GROUP BY 
        p.person_name
),
ranked_actors AS (
    SELECT 
        person_name,
        movie_count,
        RANK() OVER (ORDER BY movie_count DESC) AS rank
    FROM 
        actor_movie_counts
)
SELECT 
    person_name,
    movie_count,
    rank
FROM 
    ranked_actors
WHERE 
    rank < 10;
