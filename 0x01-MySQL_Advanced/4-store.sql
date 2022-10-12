-- this is task 4
-- creates a trigger that decreases the quantity of an item
CREATE TRIGGER `decrease`
    AFTER INSERT ON `orders`
    FOR EACH ROW
    BEGIN
      UPDATE items
           SET quantity = quantity-New.number
           WHERE name=New.item_name;
    END;