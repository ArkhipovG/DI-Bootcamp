WITH genre_movie_revenues AS (
    SELECT
        g.genre_name,
        m.movie_id,
        m.title,
        m.release_date,
        m.revenue
    FROM
        movies.movie m
    JOIN
        movies.movie_genres mg ON m.movie_id = mg.movie_id
    JOIN
        movies.genre g ON mg.genre_id = g.genre_id
)
SELECT
    genre_name,
    title,
    release_date,
    revenue,
    AVG(revenue) OVER (
        PARTITION BY genre_name
        ORDER BY release_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM
    genre_movie_revenues
ORDER BY
    genre_name, release_date;
