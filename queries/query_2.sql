SELECT gr.name AS group_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'Physics'
GROUP BY gr.name
ORDER BY avg_grade DESC;

SELECT ROUND(AVG(grade), 2) AS avg_grade_all
FROM grades;
