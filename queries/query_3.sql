SELECT t.name AS teacher, sub.name AS subject
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'John Smith';

SELECT t.name AS teacher, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.name = 'John Smith'
GROUP BY t.name;
