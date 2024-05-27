CREATE TEMPORARY TABLE avg_height_by_region (
    region_id INT,
    avg_height INT
);

INSERT INTO avg_height_by_region (region_id, avg_height)
SELECT 
	pr.region_id,
	AVG(p.height) AS avg_height
FROM 
	olympics.person p
JOIN 
	olympics.person_region pr ON p.id = pr.person_id
WHERE 
	p.height > 0
GROUP BY 
	pr.region_id

UPDATE olympics.person 
SET height = (
	SELECT
		avh.avg_height
	FROM
	avg_height_by_region avh
	JOIN
	(SELECT min(region_id) as region_id, person_id FROM olympics.person_region
group by person_id) pr ON avh.region_id = pr.region_id
	WHERE 
	pr.person_id = olympics.person.id
	)
WHERE
	height = 0

	



