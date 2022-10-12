-- this is task 11
-- creates view need_meeting that lists all students that have score under 80

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
    AND (ISNULL(last_meeting)
    OR DATEDIFF(NOW(), last_meeting) > 30);