-- this is task 4
-- creates a trigger that decreases the quantity of an item
CREATE TRIGGER `decrease`
    AFTER INSERT ON `orders`
    FOR EACH ROW
      UPDATE items
           SET quantity = quantity - NEW.number
           WHERE name = NEW.item_name;