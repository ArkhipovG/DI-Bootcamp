SELECT 
    m.medal_name,
    AVG(gc.age) AS average_age
FROM 
    olympics.competitor_event ce
JOIN 
    olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN 
    olympics.medal m ON ce.medal_id = m.id
WHERE 
    m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY 
    m.medal_name;
