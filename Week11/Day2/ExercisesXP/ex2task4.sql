WITH director_budgets AS (
    SELECT 
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
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
),
ranked_directors AS (
    SELECT 
        director_name,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) AS budget_rank
    FROM 
        director_budgets
)
SELECT 
    director_name,
    total_budget
FROM 
    ranked_directors
WHERE 
    budget_rank = 1;
