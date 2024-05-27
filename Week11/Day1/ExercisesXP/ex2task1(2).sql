CREATE TEMPORARY TABLE avg_weight_by_region (
    region_id INT,
    avg_weight INT
);


INSERT INTO avg_weight_by_region (region_id, avg_weight)
SELECT 
	pr.region_id,
	AVG(p.weight) AS avg_weight
FROM 
	olympics.person p
JOIN 
	olympics.person_region pr ON p.id = pr.person_id
WHERE 
	p.weight > 0
GROUP BY 
	pr.region_id


UPDATE olympics.person 
SET weight = (
	SELECT
		avw.avg_weight
	FROM
	avg_weight_by_region avw
	JOIN
	(SELECT min(region_id) as region_id, person_id FROM olympics.person_region
group by person_id) pr ON avw.region_id = pr.region_id
	WHERE 
	pr.person_id = olympics.person.id
	)
WHERE
	weight = 0
