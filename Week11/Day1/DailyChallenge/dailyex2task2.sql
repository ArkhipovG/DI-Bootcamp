CREATE TEMPORARY TABLE temp_persons_no_medals (
    person_id INT,
    full_name VARCHAR(255),
    games_participated INT
);

INSERT INTO temp_persons_no_medals (person_id, full_name, games_participated)
SELECT
    p.id AS person_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM
    olympics.person p
JOIN
    olympics.games_competitor gc ON p.id = gc.person_id
LEFT JOIN
	(SELECT p.id
	FROM olympics.games_competitor gc
	JOIN olympics.person p ON gc.person_id = p.id
	JOIN olympics.competitor_event ce ON gc.id = ce.competitor_id
	JOIN olympics.event e ON ce.event_id = e.id
	WHERE ce.medal_id <> 4) ce2 ON p.id = ce2.id
WHERE
	ce2.id is null
GROUP BY
    p.id, p.full_name
HAVING
    COUNT(DISTINCT gc.games_id) > 3;

SELECT * FROM temp_persons_no_medals
ORDER BY games_participated DESC