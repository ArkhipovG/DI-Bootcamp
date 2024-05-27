SELECT nr.region_name, 
	COUNT(DISTINCT(gc.id)) AS number_of_unique_competitors
	
FROM olympics.games_competitor AS gc 
	JOIN olympics.person AS p ON gc.person_id=p.id
									 
	JOIN olympics.person_region AS pr ON p.id=pr.person_id
									 
	JOIN olympics.noc_region AS nr ON nr.id = pr.region_id
WHERE gc.id IN (
	SELECT competitor_id
	FROM olympics.competitor_event
	GROUP BY competitor_id
HAVING COUNT(event_id)>3
)
GROUP BY nr.region_name
ORDER BY number_of_unique_competitors DESC
FETCH FIRST 5 ROWS ONLY;