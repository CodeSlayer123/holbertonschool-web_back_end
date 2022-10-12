-- this is task 6
--  creates stored procedure AddBonus that adds new correction for student
 DELIMITER //

CREATE
    PROCEDURE AddBonus (
        IN user_id INT,
        IN project_name VARCHAR(255),
        IN score INT
    )


DELIMITER ;
