SELECT s.id, s.name
FROM students s
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'Group A';

SELECT s.name, sub.name AS subject, g.grade, g.date_of
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE gr.name = 'Group A' AND sub.name = 'Programming'
ORDER BY s.name, g.date_of;
