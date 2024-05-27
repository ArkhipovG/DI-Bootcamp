CREATE TEMPORARY TABLE temp_competitor_analysis (
    competitor_id INT,
    person_id INT,
    full_name VARCHAR(255),
    medal_id INT
);

INSERT INTO temp_competitor_analysis (competitor_id, person_id, full_name, medal_id)
SELECT 
    gc.id AS competitor_id,
    pr.id AS person_id,
    pr.full_name,
    ce.medal_id 
FROM 
    olympics.competitor_event ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
    olympics.person pr ON gc.person_id = pr.id


DELETE FROM 
    temp_competitor_analysis
WHERE
	medal_id = 4

SELECT 
    full_name,
	COUNT(medal_id) AS total_medals
FROM 
    temp_competitor_analysis
GROUP BY full_name
ORDER BY total_medals DESC

