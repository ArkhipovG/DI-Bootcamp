-- Step 1: Create the temporary table
CREATE TEMPORARY TABLE temp_person_event_counts (
    person_id INT,
    games_id INT,
    total_events INT
);

-- Step 2: Insert the data using nested subqueries
INSERT INTO temp_person_event_counts (person_id, games_id, total_events)
SELECT 
    gc.person_id,
    gc.games_id,
    COUNT( DISTINCT ce.event_id) AS total_events
FROM 
    olympics.games_competitor gc
JOIN 
    olympics.competitor_event ce ON gc.id = ce.competitor_id
WHERE 
    gc.person_id IN (
        SELECT 
            gc_inner.person_id
        FROM 
            olympics.games_competitor gc_inner
        JOIN 
            olympics.competitor_event ce_inner ON gc_inner.id = ce_inner.competitor_id
        GROUP BY 
            gc_inner.person_id, gc_inner.games_id
        HAVING 
            COUNT(DISTINCT ce_inner.event_id) > 1
    )
GROUP BY 
    gc.person_id, gc.games_id
ORDER BY 
    gc.person_id, gc.games_id;

select p.full_name, g.games_name, tpec.total_events
from temp_person_event_counts tpec
join olympics.person p ON tpec.person_id = p.id
join olympics.games g ON tpec.games_id = g.id
order by total_events DESC