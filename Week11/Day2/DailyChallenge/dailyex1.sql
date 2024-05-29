WITH company_movie_budgets AS (
    SELECT 
        pc.company_name,
        m.movie_id,
        m.budget,
        m.release_date,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS prev_budget
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
),
budget_growth_rates AS (
    SELECT 
        company_name,
        movie_id,
        budget,
        prev_budget,
        (budget - prev_budget) / NULLIF(prev_budget, 0) AS growth_rate
    FROM 
        company_movie_budgets
    WHERE 
        prev_budget IS NOT NULL 
	)
SELECT 
    company_name,
    AVG(growth_rate) AS average_growth_rate
FROM 
    budget_growth_rates
WHERE
	growth_rate IS NOT NULL
GROUP BY 
    company_name
ORDER BY 
    average_growth_rate DESC, company_name;
