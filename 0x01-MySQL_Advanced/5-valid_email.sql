-- this is task 5
-- creates trigger that resets attribute valid_email when email is changed
DELIMITER $$

CREATE TRIGGER `reset`
    BEFORE UPDATE ON `users`
    FOR EACH ROW
    BEGIN
        IF NOT NEW.email = OLD.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END;
DELIMITER ;
