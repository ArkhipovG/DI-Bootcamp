WITH keyword_revenues AS (
    SELECT 
        k.keyword_id,
        k.keyword_name,
        m.movie_id,
        m.title,
        m.revenue
    FROM 
        movies.movie m
    JOIN 
        movies.movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN 
        movies.keyword k ON mk.keyword_id = k.keyword_id
),
series_revenues AS (
    SELECT 
        keyword_name,
        SUM(revenue) OVER (PARTITION BY keyword_name) AS total_revenue
    FROM 
        keyword_revenues
)
SELECT DISTINCT
    keyword_name AS series_name,
    total_revenue
FROM 
    series_revenues
ORDER BY 
    total_revenue DESC
LIMIT 10;
