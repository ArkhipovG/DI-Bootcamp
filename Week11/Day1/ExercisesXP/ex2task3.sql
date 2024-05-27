-- Step 1: Calculate the overall average number of medals won per person
WITH overall_avg_medals AS (
    SELECT AVG(total_medals) AS avg_medals
    FROM (
        SELECT p.id AS person_id, COUNT(ce.medal_id) AS total_medals
        FROM olympics.person p
        LEFT JOIN olympics.games_competitor gc ON p.id = gc.person_id
        LEFT JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
		WHERE ce.medal_id IN ('1','2','3')
        GROUP BY p.id
    ) overall_medals_per_person
),

-- Step 2: Calculate the average number of medals won per person for each region
region_avg_medals AS (
    SELECT region_id, AVG(total_medals) AS avg_medals
    FROM (
        SELECT pr.region_id, p.id AS person_id, COUNT(ce.medal_id) AS total_medals
        FROM olympics.person p
        LEFT JOIN olympics.person_region pr ON p.id = pr.person_id
        LEFT JOIN olympics.games_competitor gc ON p.id = gc.person_id
        LEFT JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
		WHERE ce.medal_id IN ('1','2','3')
        GROUP BY pr.region_id, p.id
    ) region_medals_per_person
    GROUP BY region_id
	)

-- Step 3: Compare averages and select regions
SELECT nr.region_name, ram.avg_medals
FROM region_avg_medals ram
JOIN olympics.noc_region nr ON ram.region_id = nr.id
WHERE avg_medals > (SELECT avg_medals FROM overall_avg_medals)
ORDER BY ram.avg_medals DESC
