SELECT DISTINCT sub.name AS subject
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN students s ON g.student_id = s.id
WHERE s.name = 'Alice Brown';

SELECT DISTINCT sub.name AS subject
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE s.name = 'Alice Brown' AND t.name = 'John Smith';
