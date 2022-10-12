-- this is task 10
-- creates function SafeDiv that divides first number by second

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
  DETERMINISTIC NO SQL READS SQL DATA
  BEGIN

    IF (b = 0) THEN
        RETURN 0;
    ELSE 
        RETURN a / b;
    END IF;

END$$
DELIMITER ;