-- CREATE TEMPORARY TABLE temp_two_sports_medals (
--     person_id INT,
--     total_medals INT
-- );

INSERT INTO temp_two_sports_medals (person_id, total_medals)
SELECT
    gc.person_id,
    COUNT(ce.medal_id) AS total_medals
FROM
    olympics.games_competitor gc
JOIN
    olympics.competitor_event ce ON gc.id = ce.competitor_id
JOIN
    olympics.games g ON gc.games_id = g.id
JOIN
    olympics.event e ON ce.event_id = e.id
JOIN
    olympics.sport s ON e.sport_id = s.id
WHERE
    ce.medal_id IN ('1', '2', '3') AND gc.person_id IN (
        SELECT
            person_id
        FROM (
            SELECT
                gc.person_id,
                COUNT(DISTINCT s.id) AS sports_count
            FROM
                olympics.games_competitor gc
            JOIN
                olympics.competitor_event ce ON gc.id = ce.competitor_id
            JOIN
                olympics.event e ON ce.event_id = e.id
            JOIN
                olympics.sport s ON e.sport_id = s.id
            GROUP BY
                gc.person_id
            HAVING
                COUNT(DISTINCT s.id) = 2
        ) AS two_sports
    )
GROUP BY
    gc.person_id;

SELECT
    p.full_name,
    ttsm.total_medals
FROM
    temp_two_sports_medals ttsm
JOIN olympics.person p ON ttsm.person_id = p.id
	
ORDER BY
    total_medals DESC
LIMIT 3;

