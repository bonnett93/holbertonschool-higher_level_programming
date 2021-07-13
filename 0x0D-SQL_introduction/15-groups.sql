-- lists the number of records with the same score in the table.
-- SQL keywords in uppercase.
SELECT score, COUNT(score) AS number
	FROM second_table
	GROUP BY score DESC;
