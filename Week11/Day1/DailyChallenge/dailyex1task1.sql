CREATE TEMPORARY TABLE temp_person_medals (
    person_id INT,
    summer_medals INT,
    winter_medals INT
);

INSERT INTO temp_person_medals (person_id, summer_medals, winter_medals)
SELECT
    p.id AS person_id,
    COALESCE(summer.medal_count, 0) AS summer_medals,
    COALESCE(winter.medal_count, 0) AS winter_medals
FROM
    olympics.person p
LEFT JOIN (
    SELECT
        gc.person_id,
        COUNT(ce.medal_id) AS medal_count
    FROM
        olympics.games_competitor gc
    JOIN
        olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN
        olympics.games g ON gc.games_id = g.id
    WHERE
        g.season = 'Summer' and ce.medal_id IN ('1', '2', '3')
    GROUP BY
        gc.person_id
) summer ON p.id = summer.person_id
LEFT JOIN (
    SELECT
        gc.person_id,
        COUNT(ce.medal_id) AS medal_count
    FROM
        olympics.games_competitor gc
    JOIN
        olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN
        olympics.games g ON gc.games_id = g.id
    WHERE
        g.season = 'Winter' and ce.medal_id IN ('1', '2', '3')
    GROUP BY
        gc.person_id
) winter ON p.id = winter.person_id
WHERE
    summer.medal_count > 0 AND winter.medal_count > 0;

SELECT p.full_name, tpm.summer_medals, tpm.winter_medals FROM temp_person_medals tpm
JOIN olympics.person p ON tpm.person_id = p.id;

