CREATE TEMPORARY TABLE temp_medal_counts (
    person_id INT,
    total_medals INT
);

INSERT INTO temp_medal_counts (person_id, total_medals)
SELECT 
    pr.id,
    COUNT(*) AS total_medals
FROM 
    olympics.competitor_event ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person pr ON gc.person_id = pr.id
WHERE 
    ce.medal_id IN ('1', '2', '3')
GROUP BY 
    pr.id
HAVING 
    COUNT(*) > 2;

SELECT 
    total_medals,
	full_name
FROM 
    temp_medal_counts tmc
JOIN
	olympics.person pr ON tmc.person_id = pr.id
ORDER BY total_medals DESC


