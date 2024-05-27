-- Subquery to find the highest number of medals won by each competitor in a single event
WITH max_medal_counts AS (
    SELECT
        ce.competitor_id,
        ce.event_id,
        COUNT(ce.medal_id) AS medal_count
    FROM
        olympics.competitor_event ce
	WHERE
        ce.medal_id IN ('1', '2', '3')
    GROUP BY
        ce.competitor_id, ce.event_id
),

-- Subquery to find the maximum medal count per competitor
competitor_max_medals AS (
    SELECT
        competitor_id,
        MAX(medal_count) AS max_medal_count
    FROM
        max_medal_counts
    GROUP BY
        competitor_id
),

-- Subquery to find the events where each competitor won the maximum number of medals
competitor_events_max_medals AS (
    SELECT
        mmc.competitor_id,
        mmc.event_id,
        mmc.medal_count
    FROM
        max_medal_counts mmc
    JOIN
        competitor_max_medals cmc
    ON
        mmc.competitor_id = cmc.competitor_id
        AND mmc.medal_count = cmc.max_medal_count
)

-- Step 2: Aggregate the Total Medals for Each Region
, region_total_medals AS (
    SELECT
        pr.region_id,
        SUM(cem.medal_count) AS total_medals
    FROM
        competitor_events_max_medals cem
    JOIN
        olympics.games_competitor gc ON cem.competitor_id = gc.id
    JOIN
        olympics.person_region pr ON gc.person_id = pr.person_id
    GROUP BY
        pr.region_id
)

-- Step 3: Display the Top 5 Regions with the Highest Total Medals
SELECT
    nr.region_name,
    rtm.total_medals
FROM
    region_total_medals rtm
JOIN
    olympics.noc_region nr ON rtm.region_id = nr.id
ORDER BY
    rtm.total_medals DESC
LIMIT 5;
