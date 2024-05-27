CREATE TEMPORARY TABLE temp_person_seasons (
    person_id INT,
    participated_in_both BOOLEAN
);

INSERT INTO temp_person_seasons (person_id, participated_in_both)
SELECT
    p.id AS person_id,
    CASE
        WHEN EXISTS (
            SELECT 1
            FROM olympics.games_competitor gc1
            JOIN olympics.games g1 ON gc1.games_id = g1.id
            WHERE gc1.person_id = p.id AND g1.season = 'Summer'
        ) AND EXISTS (
            SELECT 1
            FROM olympics.games_competitor gc2
            JOIN olympics.games g2 ON gc2.games_id = g2.id
            WHERE gc2.person_id = p.id AND g2.season = 'Winter'
        )
        THEN TRUE
        ELSE FALSE
    END AS participated_in_both
FROM
    olympics.person p;

SELECT p.full_name
FROM temp_person_seasons tps
join olympics.person p ON tps.person_id = p.id
WHERE participated_in_both = TRUE;
