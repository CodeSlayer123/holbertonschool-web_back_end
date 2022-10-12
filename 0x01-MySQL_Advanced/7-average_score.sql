-- this is task 7
-- creates stored procedure that computes and stores average score for student
DELIMITER $$

CREATE
    PROCEDURE ComputeAverageScoreForUser (
        IN user_id INT,
    )
    BEGIN
        SELECT avg( score ) FROM user_id
    END;

DELIMITER ;
