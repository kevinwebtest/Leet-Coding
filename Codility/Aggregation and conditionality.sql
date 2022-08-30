SELECT task_id, name, 
    CASE
        WHEN AVG(score) > 60 THEN 'Easy'
        WHEN AVG(score) <= 20 THEN 'Hard'
        ELSE 'Medium'
    END
 AS difficulty FROM reports AS r
JOIN tasks AS t on t.id=r.task_id
GROUP BY task_id, name
ORDER BY task_id ASC;
