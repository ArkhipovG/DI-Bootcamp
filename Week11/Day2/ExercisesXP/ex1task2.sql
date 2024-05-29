SELECT 
    pc.company_name,
    m.title,
    m.revenue,
    NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile
FROM 
    movies.movie m
JOIN 
    movies.movie_company mc ON m.movie_id = mc.movie_id
JOIN 
    movies.production_company pc ON mc.company_id = pc.company_id
ORDER BY 
    pc.company_name, quartile;
