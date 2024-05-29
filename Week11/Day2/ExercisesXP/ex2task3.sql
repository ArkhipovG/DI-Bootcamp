WITH actor_movie_revenues AS (
    SELECT 
        p.person_name,
        m.revenue
    FROM 
        movies.movie_cast mc
    JOIN 
        movies.person p ON mc.person_id = p.person_id
    JOIN 
        movies.movie m ON mc.movie_id = m.movie_id
)
SELECT 
    person_name,
    SUM(revenue) AS cumulative_revenue
FROM 
    actor_movie_revenues
GROUP BY 
    person_name
ORDER BY 
    cumulative_revenue DESC, person_name;
